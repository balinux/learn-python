# def create_html(tag,text,**atributes):
#     html = f"<{tag}>{text}</{tag}>"
#     print(atributes)
#     return html

def create_html(tag,text,**atributes):
    html = f"<{tag} "

    for key, value in atributes.items():
        html = html+f"{key}='{value}'"
    html = html + f">{text}</{tag}>"
    return html

html = create_html("p", "hello python",style = "paragraph")
print(html)

# html = create_html("a","contoh link", "google.com")
# print(html)

# contoh menggunakan keyword argument list
html = create_html("a","contoh link", href = "google.com", style="link")
print(html)
