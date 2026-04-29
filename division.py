import asyncio
from pyscript import document, window
from pyscript import when
import asciiConverter1 as ac
import abacusClass1 as a
import integerDataModel as m

# State variables
current_index = 0
page = 0
current_data = []
book = []
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

def update_ab_display():
    if book:
        # Prevent 'page' from exceeding the length of the book
        safe_page = min(page, len(book) - 1)
        document.getElementById("ab_scroll_container").innerText = book[safe_page]


def update_nb_display():
    # 1. Safety Check: If data is empty or None, abort
    if not current_data or len(current_data) == 0:
        return

    val2 = document.getElementById("input_field2").value
    container = document.getElementById("nb_scroll_container")
    images = container.getElementsByTagName('img')
    
    required_images = 2 + len(val2)
    
    while len(images) < required_images:
        container.appendChild(document.createElement('img'))
    while len(images) > required_images:
        container.removeChild(container.lastChild)

    # 2. Safety Bounds Check
    safe_idx = min(current_index, len(current_data) - 1)
    
    if safe_idx + 1 < len(current_data):
        lookahead_idx = safe_idx + 1
    else:
        lookahead_idx = safe_idx

    # 3. Safely get img_id (Protects against short '$' sublists)
    target_idx = lookahead_idx if safe_idx == 0 else safe_idx
    
    # Verify the inner list actually has at least 3 items before reading index [2]
    if len(current_data[target_idx]) > 2:
        img_id = current_data[target_idx][2]
    else:
        img_id = "0" # Fallback image ID if the list is too short
        
    # 4. Apply images to DOM
    images[0].src = f"./assets/{img_id}d.png"
    images[0].alt = "indicator"
    
    images[1].src = "./assets/b.png"
    images[1].alt = "base"
    
    for i in range(len(val2)):
        images[i + 2].src = f"./assets/{val2[i]}c.png"
        images[i + 2].alt = f"Image {i}"

def update_soFar():
    document.getElementById("output_sofar").innerText = f"output so far = {current_data[current_index][1]}"
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
'''def process_result(dub, op_char):
    global current_data, current_index, book, page, is_playing
    is_playing = False
    
    # dub[0] is the matrix/data, dub[1] is the final string result
    book = ac.flipBook(dub[2])
    page = 0
    
    current_data = dub[2]
    #window.alert(current_data)
    current_index = 0
    val1 = document.getElementById("input_field1").value
    val2 = document.getElementById("input_field2").value
    
    document.getElementById("output_label").innerText = f"{val1} {op_char} {val2} = {dub[1]}"
    document.getElementById("rods_label").innerText = f"rods: {len(dub[2][0])}"
    ls = []
    st = "\n\n"
    for c in dub[5]:
        ls.append(c)
    for c in ls:
        st = st + m.stringize(c) + "\n"
    document.getElementById("chunks_label").innerText = f"chunks: {st}"
    #document.getElementById("rods_label").innerText = f"rods: {current_data}"
    update_ab_display()
    
    update_nb_display()
    #update_soFar()
    enable_controls()
    #document.getElementById("chunks_label").innerText = f"chunks: {st}
    #container = document.getElementById("nb_scroll_container")
    
    #container.appendChild(document.getElementById("chunks_label"))'''

def process_result(dub, op_char):
    global current_data, current_index, book, page, is_playing
    is_playing = False
    
    book = ac.flipBook(dub[2])
    page = 0
    current_data = dub[2]
    current_index = 0
    
    val1 = document.getElementById("input_field1").value
    val2 = document.getElementById("input_field2").value
    
    document.getElementById("output_label").innerText = f"{val1} {op_char} {val2} = {dub[1]}"
    document.getElementById("rods_label").innerText = f"rods: {len(dub[2][0])}"
    
    # Build your chunks string
    ls = []
    st = "\n"
    for c in dub[5]:
        ls.append(c)
    for c in ls:
        st = st + m.stringize(c) + "\n"
        
    # Get the label and update the text
    chunks_elem = document.getElementById("chunks_label")
    chunks_elem.innerText = f"chunks: {st}"
    
    # Move the label inside nb_scroll_container to the very front (left side)
    container = document.getElementById("nb_scroll_container")
    container.insertBefore(chunks_elem, container.firstChild)
    
    update_ab_display()
    update_nb_display()
    enable_controls()

# --- MATH OPERATIONS ---

@when("click", "#process_button")
def div(event):
    v1, v2 = get_inputs()
    if v1: process_result(m.division(v1, v2), "÷")


# --- PLAYBACK CONTROLS ---

'''async def play_frames():
    global current_index, book, page, is_playing
    is_playing = True
    #window.alert(len(current_data))
    # Disable interaction during play
    document.getElementById("prev_button").disabled = True
    document.getElementById("next_button").disabled = True
    document.getElementById("play_button").disabled = True
    
    while is_playing and  current_index < len(current_data):
        
        
        
        if current_data[current_index][0] == "$":
            
            update_nb_display()
            update_soFar()
            current_index += 1
            
            
            #window.alert(current_index)
            
        else:
            current_index += 1
            page += 1
            update_ab_display()
            


        await asyncio.sleep(0.3)
        
    is_playing = False
    enable_controls()'''

async def play_frames():
    global current_index, book, page, is_playing
    is_playing = True
    
    # Disable interaction during play
    document.getElementById("prev_button").disabled = True
    document.getElementById("next_button").disabled = True
    document.getElementById("play_button").disabled = True
    
    while is_playing and current_index < len(current_data):
        
        # Check if the inner list actually has items before checking index [0]
        if len(current_data[current_index]) > 0 and current_data[current_index][0] == "$":
            update_nb_display()
            update_soFar()
            current_index += 1
            
        else:
            current_index += 1
            page += 1
            update_ab_display()

        await asyncio.sleep(0.3)
        
    is_playing = False
    enable_controls()

@when("click", "#play_button")
def play_click(event):
    if not is_playing and book and current_data:
        asyncio.ensure_future(play_frames())

@when("click", "#stop_button")
def stop_click(event):
    global is_playing
    is_playing = False
#for division: if current_data[current_index][0] == '$'
#then increment current_index and run update_nb_display
#we will increment both page and current_index
#@when("click", "#next_button")
#def next_click(event):

@when("click", "#next_button")
def next_click(event):
    global current_index, page
    
    # 1. Safety Check: Ensure data exists
    if not current_data or not book:
        return

    # 2. Wrapping Logic: If we are at the very last frame, reset to the start
    if current_index >= len(current_data) - 1:
        current_index = 0
        page = 0
        update_nb_display()
        update_ab_display()
        return

    # 3. STEP FORWARD FIRST!
    current_index += 1

    # 4. Now look at the frame we just stepped onto
    if len(current_data[current_index]) > 0 and current_data[current_index][0] == "$":
        # It's a bead mode frame, update the bead display
        update_nb_display()
        update_soFar() 
        
    else:
        # It's a normal math frame, increment page
        page += 1
        # Prevent page from exceeding the book length
        if page >= len(book):
            page = 0
            
        update_ab_display()

@when("click", "#prev_button")
def prev_click(event):
    global current_index, page
    
    # 1. Safety Check: Don't do anything if we are already at the beginning
    if current_index <= 0:
        #return
        current_index = len(current_data) - 1
        
    # 2. Safety Check: Ensure data actually exists
    if not current_data or not book:
        return

    # 3. REWIND FIRST! 
    # Step back so we don't check an out-of-bounds index
    current_index -= 1

    # 4. Now look at the frame we just stepped back onto
    if len(current_data[current_index]) > 0 and current_data[current_index][0] == "$":
        # It's a bead mode frame, update the bead display
        update_nb_display()
        update_soFar() 
        
    else:
        if page == 0:
            page = len(book) - 1
        # It's a normal math frame, decrement page and update abacus display
        if page > 0:
            page -= 1
        update_ab_display()

@when("click", "#clear_button")
def clear_click(event):
    global current_index, page, book, is_playing, current_data
    is_playing = False
    if book and current_data:
        page = 0
        current_index = 0
        update_nb_display()
        update_ab_display()
        document.getElementById("output_sofar").innerText = f"output so far = {current_data[1][1]}"

@when("click", "#btn_back")
def switch_mode(event):
    window.alert("Signal Emitted: Switch to Bead Mode requested.")