import os
import sys
import requests
from bs4 import BeautifulSoup
import time

try:
    from Accounts import A
except ImportError:
    print("❌ Error: Accounts.py not found!")
    sys.exit(1)

LOGIN_URL = "https://www.pythonanywhere.com/login/"

def renew(username, password, dashboard_url, account_name):
    if not username or not password:
        print(f"❌ [{account_name}] Credentials missing!")
        return False

    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
    })
    
    try:
        print(f"🔐 Logging in as {username} ({account_name})...")
        login_page = session.get(LOGIN_URL, timeout=15)
        soup = BeautifulSoup(login_page.content, 'html.parser')
        csrf_token = soup.find('input', {'name': 'csrfmiddlewaretoken'})
        
        if not csrf_token:
            print(f"❌ [{account_name}] No CSRF token")
            return False
        
        payload = {
            'csrfmiddlewaretoken': csrf_token['value'],
            'auth-username': username,
            'auth-password': password,
            'login_view-current_step': 'auth'
        }
        
        # Логинимся
        response = session.post(
            LOGIN_URL, 
            data=payload, 
            headers={'Referer': LOGIN_URL},
            timeout=15
        )
        
        # Проверка логина по наличию ссылки на выход
        if "logout" not in response.text.lower():
            print(f"❌ [{account_name}] Login failed - check credentials")
            return False
            
        print(f"✅ [{account_name}] Login successful")
        time.sleep(2)
        
        print(f"📊 [{account_name}] Accessing: {dashboard_url}")
        # ДОБАВЛЕН REFERER (защита от 403)
        dashboard = session.get(dashboard_url, headers={'Referer': LOGIN_URL}, timeout=15)
        dashboard.raise_for_status()
        
        soup = BeautifulSoup(dashboard.content, 'html.parser')
        extend_form = soup.find('form', action=lambda x: x and '/extend' in x.lower())
        
        if not extend_form:
            print(f"ℹ️  [{account_name}] No extend button (already renewed?)")
            return True
        
        extend_url = f"https://www.pythonanywhere.com{extend_form.get('action')}"
        token = extend_form.find('input', {'name': 'csrfmiddlewaretoken'})['value']

        print(f"⏰ [{account_name}] Extending...")
        result = session.post(extend_url, data={'csrfmiddlewaretoken': token}, headers={'Referer': dashboard_url})
        
        if result.status_code == 200:
            print(f"🚀 [{account_name}] SUCCESS!")
            return True
        return False

    except Exception as e:
        print(f"❌ [{account_name}] Error: {e}")
        return False

if __name__ == "__main__":
    print(f"🚀 Starting renewal for {len(A)} accounts...")
    summary = []
    
    for account in A:
        # Принудительно чистим имя и приводим к нижнему регистру для URL
        user = account['username'].strip()
        clean_url = f"https://www.pythonanywhere.com/user/{user.lower()}/webapps/"
        
        print(f"\n{'-'*40}")
        res = renew(user, account['password'].strip(), clean_url, account['name'])
        summary.append((account['name'], res))
        time.sleep(5) # Пауза побольше, чтобы PA не злился
    
    print(f"\n{'='*40}\nFINAL RESULTS:")
    all_ok = True
    for name, status in summary:
        print(f"{'✅' if status else '❌'} {name}")
        if not status: all_ok = False
    sys.exit(0 if all_ok else 1)
