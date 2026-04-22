import asyncio
from pyscript import document, window
from pyscript import when
import asciiConverter1 as ac
import abacusClass1 as a
import integerDataModel as m

# State variables
current_index = 0
current_data = []
is_playing = False

def checkInput(inp):
    if not inp: return False
    if ord(inp[0]) == 48 and len(inp) > 1:
        return False
    for char in inp:
        if ord(char) < 48 or ord(char) > 57:
            return False
    return True

def enable_controls():
    document.getElementById("prev_button").disabled = False
    document.getElementById("next_button").disabled = False
    document.getElementById("clear_button").disabled = False
    document.getElementById("play_button").disabled = False
    document.getElementById("stop_button").disabled = False
#def update_ab_display, and def update_nb_display for division
'''update_ab_display():
    if current_data:
        document.getElementById("ab_scroll_container").innerText = book[current_index]
    update_nB_display():
    if current_data:
        document.getElementById("nb_scroll_container").innerText = current_data[current_index]'''
def update_display():
    if current_data:
        document.getElementById("scroll_container").innerText = current_data[current_index]

def get_inputs():
    v1 = document.getElementById("input_field1").value
    v2 = document.getElementById("input_field2").value
    if not (checkInput(v1) and checkInput(v2)):
        window.alert("Please enter valid positive integers.")
        return None, None
    return v1, v2
#division will have current_data be dub[0] 
#and book will be ac.flipBook(dub[0])
#actually I think I need to add something 
#to asciiConverter1 to ignore
#sublists with $ at index 0
#book and current_data will have different sizes
#and so be indexed differently?
#I should move this code into it's own file
#and put the nigel cheese stuff into my essay.
#division will have one math button but the same control buttons.
def process_result(dub, op_char):
    global current_data, current_index, is_playing
    is_playing = False
    
    # dub[0] is the matrix/data, dub[1] is the final string result
    current_data = ac.flipBook(dub[0])
    current_index = 0
    
    val1 = document.getElementById("input_field1").value
    val2 = document.getElementById("input_field2").value
    
    document.getElementById("output_label").innerText = f"{val1} {op_char} {val2} = {dub[1]}"
    document.getElementById("rods_label").innerText = f"rods: {len(dub[0][0])}"
    
    update_display()
    enable_controls()

# --- MATH OPERATIONS ---

@when("click", "#process_button")
def regAdd(event):
    v1, v2 = get_inputs()
    if v1: process_result(m.regAdd(v1, v2), "+")

@when("click", "#process_button2")
def adiro(event):
    v1, v2 = get_inputs()
    if v1: process_result(m.adiro(v1, v2), "+")

@when("click", "#process_button3")
def minus(event):
    v1, v2 = get_inputs()
    if v1: process_result(m.minus(v1, v2), "-")

@when("click", "#process_button4")
def sudiro(event):
    v1, v2 = get_inputs()
    if v1:
        dub = m.sudiro(v1, v2)
        if len(dub) == 1:
            window.alert("For sudiro the first number must be larger than the second.")
            return
        process_result(dub, "-")

@when("click", "#process_button5")
def mCNS(event):
    v1, v2 = get_inputs()
    if v1:
        dub = m.MultCNS(v1, v2)
        # Note: MultCNS returns (result_str, data) unlike the others
        process_result((dub[1], dub[0]), "×")

@when("click", "#process_button6")
def mJPS(event):
    v1, v2 = get_inputs()
    if v1:
        dub = m.multJPS(v1, v2)
        process_result((dub[1], dub[0]), "×")

# --- PLAYBACK CONTROLS ---

async def play_frames():
    global current_index, is_playing
    is_playing = True
    
    # Disable interaction during play
    document.getElementById("prev_button").disabled = True
    document.getElementById("next_button").disabled = True
    document.getElementById("play_button").disabled = True
    
    while is_playing and current_index < len(current_data) - 1:
        current_index += 1
        update_display()
        await asyncio.sleep(0.3)
        
    is_playing = False
    enable_controls()

@when("click", "#play_button")
def play_click(event):
    if not is_playing and current_data:
        asyncio.ensure_future(play_frames())

@when("click", "#stop_button")
def stop_click(event):
    global is_playing
    is_playing = False
#for division: if current_data[current_index][0] == '$'
#then
@when("click", "#next_button")
def next_click(event):
    global current_index
    if current_data:
        current_index = (current_index + 1) % len(current_data)
        update_display()

@when("click", "#prev_button")
def prev_click(event):
    global current_index
    if current_data:
        current_index = (current_index - 1) % len(current_data)
        update_display()

@when("click", "#clear_button")
def clear_click(event):
    global current_index, is_playing
    is_playing = False
    if current_data:
        current_index = 0
        update_display()

@when("click", "#btn_back")
def switch_mode(event):
    window.alert("Signal Emitted: Switch to Bead Mode requested.")