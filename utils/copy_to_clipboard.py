import tkinter as tk

def copy_to_clipboard(window, widget, add_prompt=False, prompt_state=None, prompt_text_widget=None):

    # Initialize prompt content
    prompt_content = ""
    if add_prompt and prompt_state and prompt_text_widget:
        prompt_content = prompt_text_widget.get("1.0", "end-1c") + "\n\n"

    # Determine widget content
    if isinstance(widget, tk.Entry):
        value_to_copy = widget.get()
    elif isinstance(widget, tk.Text):
        value_to_copy = widget.get("1.0", "end-1c")
    else:
        value_to_copy = ""

    # Combine prompt content and widget content
    value_to_copy = prompt_content + value_to_copy

    # Access and set clipboard
    window.clipboard_clear()
    window.clipboard_append(value_to_copy)
    window.update_idletasks()  # Ensures clipboard content is updated
