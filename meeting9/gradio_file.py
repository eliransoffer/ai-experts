import gradio as gr


def calc_area(my_file):
    print(type(my_file))
    print(my_file)
    counter = 0
    with open(my_file) as f:
        for line in f:
            counter += 1
    return f"Lines number: {counter}"


demo = gr.Interface(
    fn=calc_area,
    inputs=["file"],
    # inputs=["number", "number"],
    # inputs=[Number(label="Insert width:"), Number(label="Insert height")],
    outputs=["text"],
    flagging_mode="never",
)


demo.launch(share=False)
