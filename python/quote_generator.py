import tkinter as tk
import requests
#Had to learn this in order for the quote API to work, basically bypasses the unsafe warning
#Importing the url library in order for the bypass to work
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def quote_generator():
    global quote, author
    try:
        #Gets the quote through the API (removing verify since it was causing errors)
        response = requests.get("https://api.quotable.io/random", verify=False)
        #Why status code 200? Because that's the code for the correct JSON response
        if response.status_code == 200:
            #Turns the response into data (or just a variable to simplify)
            data = response.json()
            try:
                #Gets required data
                quote = data["content"]
                author = data["author"]
                #This except catches the error when the API response doesn't contain the expected keys,
                #like "content" or "author". If the structure of the response is not as expected 
                #(e.g., if the API sends a different format), it will raise a KeyError.
            except KeyError:
                #Clears the existing content in quote_space, which is where the quote is displayed
                quote_space.delete("1.0", tk.END)
                #Inserts a message into quote_space informing the user that the response format from the API was not as expected.
                quote_space.insert(tk.END, "Unexpected response format.")
                return
            #Clears any quote before the new one
            quote_space.delete("1.0", tk.END)
            #Displays the quote
            quote_space.insert(tk.END, quote)
        #This else is executed when the API request is successful (if the response status code is 200),
        #but there is an issue with the quote data itself (such as missing fields or data corruption).
        #If the KeyError is not triggered, but the API data is not correctly structured, the code in the else will run.    
        else:
            #Clears any existing text in quote_space
            quote_space.delete("1.0", tk.END)
            #Generic message in case it doesn't work, and telling them to try fetching another one
            quote_space.insert(tk.END, "Failed to fetch quote. Try again.")
    except Exception as e:
        quote_space.delete("1.0", tk.END)
        quote_space.insert(tk.END, f"Error: {e}")

            

def quote_remover():
    quote_space.delete("1.0", tk.END)
    author_space.delete("1.0", tk.END)

def quote_author():
    # Displays the author's name in the author_space text box
    # Clears any previous text
    author_space.delete("1.0", tk.END)
    # Inserts the author's name
    author_space.insert(tk.END, author)

window = tk.Tk()

window.geometry("600x400")

quote_space = tk.Text(window, height = 3, width = 45, font = ("Arial", 18))
quote_space.grid(columnspan = 5)

author_label = tk.Label(window, text="Quote from: ", font=("Arial", 18), fg="gray")
author_label.grid(column = 0, row = 2, columnspan = 2)

author_space = tk.Text(window, height = 1, width = 20, font = ("Arial", 22))
author_space.grid(column = 0, row = 2, columnspan = 5)

quote_btn = tk.Button(window, text = "Get Random Quote", command = quote_generator, width= 20, font = ("Arial", 14))
quote_btn.grid(column = 2, row = 4)
erase_btn = tk.Button(window, text = "Remove Quote", command = quote_remover, width= 20, font = ("Arial", 14))
erase_btn.grid(column = 2, row = 5)
author_btn = tk.Button(window, text = "Quote's Author", command = quote_author, width= 20, font = ("Arial", 14))
author_btn.grid(column= 2, row = 6)

window.mainloop()