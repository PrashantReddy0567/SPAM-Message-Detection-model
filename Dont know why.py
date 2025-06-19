import pandas as pd

# 📂 Step 1: Load your SMS data
df = pd.read_csv('sms_data_updated.csv')

# ✅ If category column doesn't exist, add it
if 'category' not in df.columns:
    df['category'] = ''

# 🚩 Step 2: Define spam word list (simple but effective)
spam_words = [
    'free', 'win', 'offer', 'click', 'urgent', 'bonus', 'prize', 'guarantee',
    'limited', 'act now', 'buy', 'cheap', 'discount', 'congratulations',
    'loan', 'credit', 'cash', 'deal', 'exclusive', 'promotion'
]

def is_spam(message):
    message = str(message).lower()
    return any(word in message for word in spam_words)

# 🕯️ Step 3: Loop through messages and ask for manual label
for i, row in df.iterrows():
    # Skip if already labeled
    if row['category']:
        continue
    
    print(f"\n📩 Message {i+1}/{len(df)}:")
    print(f"From: {row['_address']}")
    print(f"Text: {row['_body']}")
    
    # 🚩 Suggest spam if detected
    if is_spam(row['_body']):
        print("⚠️  This message looks like SPAM! (based on keywords)")

    # 🏷️ Ask user for category
    print("Categories: food, Payments, otp, travel, spam, contacts ")
    category = input("Enter category: ").strip().lower()
    
    # Save label
    df.at[i, 'category'] = category

    # 📝 Optional: Save every 10 steps (auto-save safety)
    if i % 10 == 0:
        df.to_csv('sms_data_labeled.csv', index=False)

# 🛡️ Step 4: Save the final labeled dataset
df.to_csv('sms_data_labeled.csv', index=False)
print("\n✅ All messages labeled and saved to sms_data_labeled.csv!")
