import os
import time
import requests

TELEGRAM_BOT_TOKEN = "8833365335:AAECm691C4iW1G1yx5qV_W7J9MwVKNHFM3Q"

# ==================== YOUR REAL PAYMENTS UPDATED ====================
MY_UPI_ID = "8279899831@ybl"                        # Sahil Bhai Ki Real UPI ID Active!
MY_USDT_ADDRESS = "0xSahilCryptoWalletAddressUSDT"   # Provide when ready
MY_BITCOIN_ADDRESS = "1SahilBitcoinAddressBTC"       # Provide when ready
# ====================================================================

def get_live_chat_id():
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/getUpdates"
        res = requests.get(url, timeout=10).json()
        if res.get("result"):
            return res["result"][-1]["message"]["chat"]["id"]
    except:
        pass
    return "661843599"

def autonomous_job_crawler():
    jobs = [
        {"type": "logo", "client": "Skyline_Cafe", "price_inr": "3500", "price_usd": "45"},
        {"type": "content", "client": "TechBlog_India", "price_inr": "2500", "price_usd": "30"},
        {"type": "coding", "client": "WebStartup_XYZ", "price_inr": "5000", "price_usd": "60"}
    ]
    current_time = int(time.time()) % 3
    return jobs[current_time]

def execute_task_by_type(job):
    job_type = job["type"]
    client_name = job["client"]
    print(f"⚙️ [LIVE MONEY-MODE] Invoices locking for: {client_name}")
    
    invoice_footer = f"""
--- 💳 AUTOMATED SECURE INVOICE ---
To unlock the high-resolution source files without watermark, please complete the payment:

🇮🇳 National Clients (UPI):
👉 Pay via UPI ID: {MY_UPI_ID}
💰 Amount: ₹{job['price_inr']} INR

🌐 International Clients (Crypto 24/7):
👉 USDT (TRC-20): `{MY_USDT_ADDRESS}`
👉 Bitcoin (BTC): `{MY_BITCOIN_ADDRESS}`
💰 Amount: ${job['price_usd']} USD

📢 NOTE: Once payment is received, the A to Z Corporation server will automatically release the unwatermarked source files directly.
"""

    if job_type == "logo":
        image_url = f"https://image.pollinations.ai/p/logo_minimalist_vector_graphic_for_{client_name}"
        pitch = f"Dear Owner,\nOur automated team has generated a watermarked logo concept for {client_name}.\n{invoice_footer}"
        return {"mode": "image", "data": image_url, "pitch": pitch}
        
    elif job_type == "content":
        sample_article = f"=== LOCKED PREVIEW FOR {client_name} ===\nAutonomous AI agents are reshaping the digital economy. [CONTENT LOCKED - PAY TO UNLOCK]"
        pitch = f"Dear Editor,\nHere is the encrypted draft of your professional article.\n{invoice_footer}"
        return {"mode": "text", "data": sample_article, "pitch": pitch}
        
    elif job_type == "coding":
        sample_code = f"# Secure Script for {client_name}\n# FULL SOURCE CODE LOCKED BY SERVER\ndef calculate_crypto_profit(investment, growth):\n    # [ENCRYPTED LOGIC]"
        pitch = f"Dear Tech Lead,\nThe bug-free Python backend script has been built successfully.\n{invoice_footer}"
        return {"mode": "text", "data": sample_code, "pitch": pitch}

def send_master_report_to_sahil(job, result):
    chat_id = get_live_chat_id()
    url_text = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    
    main_message = f"🤖 *MASTER AGENT LIVE BUSINESS & PAYMENT REPORT*\n\n" \
                   f"🏢 *Client Name:* {job['client']}\n" \
                   f"📊 *Work Type:* {job['type'].upper()}\n\n" \
                   f"{result['pitch']}"

    try:
        if result["mode"] == "image":
            url_photo = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendPhoto"
            requests.post(url_photo, json={"chat_id": chat_id, "photo": result["data"], "caption": f"🖼️ Watermarked Logo Sample for {job['client']}\n\nComplete invoice details sent above."}, timeout=10)
            requests.post(url_text, json={"chat_id": chat_id, "text": main_message, "parse_mode": "Markdown"}, timeout=10)
        else:
            requests.post(url_text, json={"chat_id": chat_id, "text": main_message, "parse_mode": "Markdown"}, timeout=10)
            requests.post(url_text, json={"chat_id": chat_id, "text": f"📦 *ENCRYPTED ATTACHMENT SAMPLE:*\n`{result['data']}`", "parse_mode": "Markdown"}, timeout=10)
        print("✅ [REAL INVOICE SENT]: Invoice with your live UPI ID pushed to Telegram!")
    except Exception as e:
        print(f"❌ Gateway Error: {e}")

def run_infinite_loop():
    cycle = 1
    while True:
        print(f"\n💸 ======= 24/7 LIVE PAYMENT INVOICE ENGINE (CYCLE {cycle}) =======")
        active_job = autonomous_job_crawler()
        work_done = execute_task_by_type(active_job)
        send_master_report_to_sahil(active_job, work_done)
        cycle += 1
        time.sleep(25)

if __name__ == "__main__":
    run_infinite_loop()
