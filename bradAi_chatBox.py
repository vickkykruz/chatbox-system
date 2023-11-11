from bardapi import Bard
import gradio as gr

token = 'dAjklC68Ph8X8mbW4ynNA0GH2FePSBj35jcsIQ-iKqWkIIi_XuWZ7D7Yd773DVsyvh4zPQ.'
bard = Bard(token=token)

def chatBrandBox(question, bard=bard):
    
    return bard.get_answer(question)['content']

demo = gr.Interface(fn=chatBrandBox, inputs="text", outputs="text", title="An AI ChatBox System",
                    description="Hey Victor. This program collects whatever qusetion you want to ask then gives out an output to that question\
                        immdiatey", theme=gr.themes.Default(font=[gr.themes.GoogleFont("Inconsolata"), "Arial", "sans-serif"]))
demo.launch(share=True)