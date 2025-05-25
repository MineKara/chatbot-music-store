import streamlit as st
import requests
import re

# Configuration
API_URL = "http://localhost:8000/ask"
IMAGE_PATTERN = r'(https?://\S+\.(?:png|jpg|jpeg|gif))'

# Page setup
st.set_page_config(
    page_title="The Guitar Emporium AI",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for Vintage Music Shop Theme
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=League+Spartan:wght@700&family=Merriweather:wght@300;400;700&display=swap');

        body, .stApp {
            background-color: #fdfaf6 !important; /* Warm off-white, like aged paper */
            color: #4a3b31 !important; /* Dark warm brown for text */
            font-family: 'Merriweather', serif !important;
        }

        .main-content-wrapper {
            max-width: 900px;
            margin: 2rem auto;
            padding: 1rem;
        }
        
        .header-section {
            text-align: center;
            margin-bottom: 3rem;
            padding: 2rem 0;
            border-bottom: 2px solid #d4a017; /* Mustard yellow accent */
        }

        .main-title {
            font-family: 'League Spartan', sans-serif !important;
            font-size: 3.5rem;
            font-weight: 700;
            color: #4a3b31; /* Dark warm brown */
            text-transform: uppercase;
            letter-spacing: 2px;
            margin-bottom: 0.5rem;
        }

        .subtitle {
            font-family: 'Merriweather', serif !important;
            font-size: 1.2rem;
            color: #7a6a5d; /* Softer brown */
            font-style: italic;
            margin-bottom: 1.5rem;
        }

        .search-area {
            background-color: #fffdfa; /* Slightly lighter cream */
            border: 1px solid #e0d8cc;
            border-radius: 8px;
            padding: 2rem;
            margin-bottom: 2.5rem;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        }

        /* Target Streamlit's text input specifically */
        div[data-testid="stTextInput"] > label {
            color: #4a3b31 !important;
            font-family: 'League Spartan', sans-serif !important;
            font-size: 1.2rem !important;
            font-weight: 700 !important;
            margin-bottom: 0.75rem !important;
        }
        div[data-testid="stTextInput"] > div > div > input {
            background-color: #ffffff !important;
            color: #4a3b31 !important;
            border: 1px solid #c8bba_long_string_removed!important;
            border-radius: 6px !important;
            padding: 0.75rem 1rem !important;
            font-family: 'Merriweather', serif !important;
            font-size: 1rem !important;
            box-shadow: none !important;
        }
        div[data-testid="stTextInput"] > div > div > input:focus {
            border-color: #d4a017 !important; /* Mustard yellow focus */
            box-shadow: 0 0 0 2px rgba(212, 160, 23, 0.2) !important;
        }

        .example-text {
            color: #7a6a5d;
            font-size: 0.9rem;
            margin-top: 1rem;
            font-style: italic;
        }
        
        .response-display-area {
            margin-top: 2rem;
        }

        .product-card {
            background-color: #fffdfa; /* Light cream background for cards */
            border: 1px solid #e0d8cc;
            border-radius: 8px;
            padding: 1.5rem;
            margin-bottom: 2rem;
            box-shadow: 0 3px 10px rgba(0,0,0,0.07);
        }

        .product-title {
            font-family: 'League Spartan', sans-serif !important;
            font-size: 1.8rem;
            font-weight: 700;
            color: #d4a017; /* Mustard yellow accent */
            margin-bottom: 1rem;
        }

        .product-image-container img {
            border-radius: 6px;
            width: 100%;
            max-width: 350px; /* Control image size */
            height: auto;
            margin: 0 auto 1rem auto;
            display: block;
            border: 1px solid #eee5d8;
        }

        .product-details-text {
            color: #5c4d41;
            font-size: 0.95rem;
            line-height: 1.7;
            padding: 0.5rem;
            background-color: #fdf7f0; /* Very light contrasting bg for details */
            border-left: 3px solid #d4a017;
            border-radius: 0 4px 4px 0;
        }
        
        .loading-text {
            font-family: 'League Spartan', sans-serif !important;
            color: #d4a017;
            font-size: 1.2rem;
            text-align: center;
            padding: 2rem 0;
        }
        .stSpinner > div {
             border-top-color: #d4a017 !important; /* Mustard for spinner */
        }

        .custom-error,
        .custom-info {
            padding: 1rem;
            border-radius: 6px;
            margin: 1rem 0;
            font-size: 0.95rem;
            border-left-width: 4px;
        }
        .custom-error {
            background-color: #fcede8 !important; /* Light error bg */
            border-color: #c0392b !important; /* Error accent */
            color: #782c25 !important;
        }
        .custom-info {
            background-color: #e8f6f3 !important; /* Light info bg */
            border-color: #16a085 !important; /* Info accent */
            color: #117864 !important;
        }
        
        #MainMenu, footer, header, .stDeployButton {
            display: none !important;
        }

    </style>
""", unsafe_allow_html=True)

# --- App Layout Starts Here ---
st.markdown('<div class="main-content-wrapper">', unsafe_allow_html=True)

# Header
st.markdown("""
    <div class="header-section">
        <div class="main-title">The Guitar Emporium</div>
        <div class="subtitle">AI-Powered Pickup Finder: Discover Your Perfect Tone</div>
    </div>
""", unsafe_allow_html=True)

# Search Input (no extra wrapper)
user_query = st.text_input(
    "What axe are you hunting for?", 
    key="user_query_vintage", 
    placeholder="e.g., 'Vintage Telecasters' or 'High-gain humbuckers'"
)
st.markdown('<p class="example-text">✨ Try: "Show me blue Strats" or "What are some good jazz guitars?"</p>', unsafe_allow_html=True)

# Results Display Area
if user_query:
    st.markdown('<div class="response-display-area">', unsafe_allow_html=True)
    with st.spinner(''): # Spinner text handled by CSS styled p.loading-text
        st.markdown('<p class="loading-text"> strumming through our collection...</p>', unsafe_allow_html=True)
        try:
            payload = {"question": user_query}
            response = requests.post(API_URL, json=payload)
            response.raise_for_status()
            api_response_data = response.json()
            answer_text = api_response_data.get("answer", "")

            if not answer_text.strip():
                st.markdown('<div class="custom-info">Seems a bit quiet... Try asking another way?</div>', unsafe_allow_html=True)
            else:
                parts = re.split(f'({IMAGE_PATTERN})', answer_text)
                # Filter out empty strings that can result from re.split
                parts = [part for part in parts if part.strip()] 
                found_guitars_structured = False
                
                # Consolidate text parts that appear before the first image or if no images exist.
                # This helps prevent fragmented text display for non-image responses.
                if not any(re.fullmatch(IMAGE_PATTERN, p) for p in parts):
                    # If no images at all, just display the whole answer_text as one block.
                    st.markdown(f'<div class="product-details-text" style="margin-bottom:1rem;">{answer_text}</div>', unsafe_allow_html=True)
                else:
                    current_text_block = []
                    for i in range(len(parts)):
                        part = parts[i]
                        if re.fullmatch(IMAGE_PATTERN, part):
                            found_guitars_structured = True
                            
                            # Display accumulated text before this image as product name/description
                            if current_text_block:
                                combined_text = " ".join(current_text_block).strip()
                                # Attempt to derive a name more intelligently
                                name_lines = [line.strip() for line in combined_text.split('\n') if line.strip()]
                                product_name = name_lines[-1] if name_lines else "Featured Guitar"
                                # Clean up common prefixes from name for display
                                product_name = re.sub(r"^(Name:|Product:|Here is the|Here's a)\s*", '', product_name, flags=re.IGNORECASE).strip()
                                
                                st.markdown('<div class="product-card">', unsafe_allow_html=True)
                                st.markdown(f'<div class="product-title">{product_name}</div>', unsafe_allow_html=True)
                                # Display the rest of the text block if it wasn't just the name
                                if len(name_lines) > 1:
                                    st.markdown(f'<div class="product-details-text" style="margin-bottom:1rem;">{" ".join(name_lines[:-1])}</div>', unsafe_allow_html=True)
                                current_text_block = [] # Reset for next product
                            else: # No preceding text, still need a card and title for the image
                                st.markdown('<div class="product-card">', unsafe_allow_html=True)
                                st.markdown(f'<div class="product-title">Featured Guitar</div>', unsafe_allow_html=True)

                            st.markdown(f'<div class="product-image-container"><img src="{part}" alt="Guitar Image"></div>', unsafe_allow_html=True)
                            # Product card is closed after potential details from next text part
                        else: # It's a text part
                            current_text_block.append(part)

                        # If this is the last part and it's text (or if an image was just processed and next is text for its details)
                        # or if an image was just processed and there are no more parts
                        if (i == len(parts) - 1 and current_text_block) or \
                           (re.fullmatch(IMAGE_PATTERN, parts[i-1] if i > 0 else "") and current_text_block):
                            if found_guitars_structured:
                                # This text belongs to the product card of the preceding image
                                st.markdown(f'<div class="product-details-text">{" ".join(current_text_block).strip()}</div>', unsafe_allow_html=True)
                                st.markdown('</div>', unsafe_allow_html=True) # Close product-card
                                current_text_block = []
                            # If it's the very last part and no images were ever found, this case is handled by the initial check.

                    # If there was any leftover text after the loop (e.g. last part was text, but not associated with an image card yet)
                    if current_text_block and not found_guitars_structured:
                        # This text wasn't associated with any image, display it generally
                        st.markdown(f'<div class="product-details-text" style="margin-bottom:1rem;">{" ".join(current_text_block).strip()}</div>', unsafe_allow_html=True)

                # Fallback message if parsing didn't yield structured guitars but LLM might indicate no results
                no_guitars_keywords = ["no matching guitars", "couldn't find any guitars", "no guitars in stock matching"]
                if not found_guitars_structured and any(keyword in answer_text.lower() for keyword in no_guitars_keywords):
                    st.markdown('<div class="custom-info">🤔 Couldn\'t find that specific model. How about trying a different search?</div>', unsafe_allow_html=True)
        
        except requests.exceptions.HTTPError as http_err:
            error_detail = http_err.response.text if hasattr(http_err, 'response') and http_err.response else str(http_err)
            if hasattr(http_err, 'response') and http_err.response is not None and http_err.response.status_code == 429:
                st.markdown('<div class="custom-error">⏳ Looks like we\'re hitting the strings too hard! API rate limit exceeded. Please try again shortly.</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="custom-error">📡 Houston, we have a problem... (HTTP Error: {error_detail})</div>', unsafe_allow_html=True)
        except requests.exceptions.RequestException as e:
            st.markdown(f'<div class="custom-error">🔌 Can\'t connect to the amp! Check if the AI assistant is plugged in. ({str(e)})</div>', unsafe_allow_html=True)
        except Exception as e:
            st.markdown(f'<div class="custom-error">⚠️ Oops! A string broke (Unexpected error: {str(e)})</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True) # Close response-display-area

st.markdown('</div>', unsafe_allow_html=True) # Close main-content-wrapper
