import gradio as gr
from gradio import Number

my_output = ""

def calc_area(width, height):
    my_output = f"The area is {width*height}"
    result = width * 30
    return f"The area is {width*height}", 0


demo = gr.Interface(
    fn=calc_area,
    inputs=[Number(value=10, label="Width", minimum=10, maximum=100), "number"],
    outputs=["text", "number"],
    title="MY best app",
    # theme="soft"
    theme="monochrome",

)


if __name__ == "__main__":
    demo.launch(share=False)