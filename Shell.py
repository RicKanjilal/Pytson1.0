import basic
import webbrowser

while True:
    text = input('>>>> ')
    text = text.upper()
    if text == "TRMINATE":
        break
    elif text == 'PS INSTALL SEARCH':
        print('search is installed your program')
    elif "how are you" or "how are you doing" or "how are you Pytson" or "how" in text:
        print('I am fine thank you for asking')
    elif "hi" or "hello" or "hola " or "hey" in text:
        print('hey there')
    elif text == 'INTERNET.BIG':
        import SEARCH
    elif text == 'PS INSTALL INTERNET':
        print('internet is installed your program')
    elif "INTERNET.SMALL" in text:
        sea = text.replace("INTERNET.SMALL", "")
        webbrowser.open_new_tab(sea)
    elif text.strip() == "":
        continue
    result, error = basic.run('<stdin>', text)

    if error:
        print(error.as_string())
    elif result:
        if len(result.elements) == 1:
            print(repr(result.elements[0]))
        else:
            print(repr(result))
