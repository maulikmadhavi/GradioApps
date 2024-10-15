import gradio as gr
import pandas as pd

# Function to calculate tax and update the dataframe
def calculator(income, df):
    tax = round(income * 0.2)
    # new_row = pd.DataFrame({"Income": [income], "Tax": [tax]})
    try:
     old_incomes = [ income] + df.Income.tolist()
     old_tax =  [tax] + df.Tax.tolist() 
    except:
      old_incomes = [income]
      old_tax = [tax]
   

    df = pd.DataFrame({
      "Income": old_incomes,
      "Tax" : old_tax
    })
    return df

# Initialize the dataframe with an empty state
df_state = pd.DataFrame(columns=["Income", "Tax"])

with gr.Blocks() as demo:
    income_input = gr.Number(label="Income")
    calculate_button = gr.Button("Calculate ") 
    tax_output = gr.Dataframe(
        label="Calculation",
        value=df_state,
        headers=["Income", "Tax"],  # Explicitly specify column headers
        datatype=["number", "number"],  # Explicitly set datatype for each column
        visible=True
    )
   
    
    # Connect the button click to the tax_calculator function and update the dataframe
    calculate_button.click(fn=calculator, inputs=[income_input, tax_output], outputs=tax_output)

demo.launch(show_error=True)