!pip install gtts ipywidgets
import ipywidgets as widgets
from IPython.display import display, Audio
from gtts import gTTS
import os

# Function to convert text to speech
def text_to_speech(text, lang, tld, slow):
    tts = gTTS(text=text, lang=lang, tld=tld, slow=slow)
    audio_file = "output.mp3"
    tts.save(audio_file)
    return audio_file

# Function to handle button click
def on_button_click(b):
    # Get the input values
    text = text_input.value
    lang = lang_dropdown.value
    tld = tld_dropdown.value
    slow = slow_checkbox.value
    
    # Generate speech and display it
    audio_file = text_to_speech(text, lang, tld, slow)
    display(Audio(audio_file, autoplay=True))

# Text input widget
text_input = widgets.Textarea(
    value='Enter your text here...',
    placeholder='Type something',
    description='Text:',
    disabled=False
)

# Language dropdown widget
lang_dropdown = widgets.Dropdown(
    options=[('English', 'en'), ('Spanish', 'es'), ('French', 'fr'), ('German', 'de')],
    value='en',
    description='Language:',
    disabled=False
)

# Voice dropdown widget (selecting different top-level domains for accents)
tld_dropdown = widgets.Dropdown(
    options=[('Default', 'com'), ('India', 'co.in'), ('UK', 'co.uk'), ('US', 'us'), ('Canada', 'ca')],
    value='com',
    description='Accent:',
    disabled=False
)

# Slow speech checkbox
slow_checkbox = widgets.Checkbox(
    value=False,
    description='Slow Speech',
    disabled=False
)

# Button to generate speech
generate_button = widgets.Button(
    description='Generate Speech',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Click to generate speech',
    icon='play'
)
generate_button.on_click(on_button_click)

# Display widgets
display(text_input, lang_dropdown, tld_dropdown, slow_checkbox, generate_button)
