import ui, flash, zenhan
from janome.tokenizer import Tokenizer

def flash_message(sender):
	textview = sender.superview['textview']
	source = textview.text
	
	slider = sender.superview['slider']
	speed = (.1 + slider.value) / 10
	tokenizer = Tokenizer()
	tokens = tokenizer.tokenize(source)

	word = ''
	for token in tokens:
		if token.reading == '*':
			word += token.surface
		else:
			word += token.reading
	
	word = word.upper()
	word = zenhan.h2z(word)
	textview.text = word
	
	
	flash.flash_signals(word, speed)
v = ui.load_view()
v.present('sheet')


