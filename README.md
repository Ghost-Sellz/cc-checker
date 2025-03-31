# Stripe CC Checker

## Description
This script checks credit card validity using the Stripe API. It reads card details from a file (`cc.txt`), processes them, and saves the results in `results.txt`.

## Features
✅ Reads credit cards from `cc.txt`  
✅ Uses Stripe API to verify cards  
✅ Saves results to `results.txt`  
✅ Handles errors & invalid formats  

## Requirements
- Python 3.x
- Stripe API key
- `stripe` Python library

## Installation
1. Clone the repository or download the script.
   ```bash
   git clone https://github.com/ghost-sellz/cc-checker
   cd cc-checker
   ```

2. Install required dependencies.
   ```bash
   pip install -r requirements.txt
   ```

3. Edit the script and replace `your_key_goes_here` with your Stripe **secret key**.

## Usage
1. Add credit card details to `cc.txt` in this format:
   ```
   4242424242424242 | 12 | 2025 | 123
   4000056655665556 | 11 | 2024 | 456
   ```
2. Run the script:
   ```bash
   python main.py
   ```
3. Results will be saved in `results.txt`.

## Output Format
Each line in `results.txt` will show the card status:
```
4242424242424242 | 12 | 2025 | 123 - Approved ✅
4000056655665556 | 11 | 2024 | 456 - Declined ❌ (Card declined)
```

## Warning ⚠️
- **i am NOT hold accountable for what you do with this tool**

## License
MIT License

