import time
from objc_util import ObjCClass

signals ={'ア':33133,'イ':13,'ウ':113,'エ':31333,'オ':13111}
signals.update({'カ':1311,'キ':31311,'ク':1113,'ケ':3133,'コ':3333})
signals.update({'サ':31313,'シ':33131,'ス':33313,'セ':13331,'ソ':3331})
signals.update({'タ':31,'チ':1131,'ツ':1331,'テ':13133,'ト':11311})
signals.update({'ナ':131,'ニ':3131,'ヌ':1111,'ネ':3313,'ノ':1133})
signals.update({'ハ':3111,'ヒ':33113,'フ':3311,'ヘ':1,'ホ':311})
signals.update({'マ':3113,'ミ':11313,'ム':3,'メ':31113,'モ':31131})
signals.update({'ヤ':133,'ユ':31133,'ヨ':33})
signals.update({'ラ':111,'リ':331,'ル':31331,'レ':333,'ロ':1313})
signals.update({'ワ':313,'ヲ':1333,'ン':13131})
signals.update({'ヰ':13113,'゛':11,'゜':11331,'ー':13313,'ヴ':113011})
signals.update({'ガ':1311011,'ギ':31311011,'グ':1113011,'ゲ':3133011,'ゴ':3333011})
signals.update({'ザ':31313011,'ジ':33131011,'ズ':33313011,'ゼ':13331011,'ゾ':3331011})
signals.update({'ダ':31011,'ジ':1131011,'ヅ':1331011,'デ':13133011,'ド':11311011})
signals.update({'バ':3111011,'ビ':33113011,'ブ':3311011,'ベ':1011,'ボ':311011})
signals.update({'ァ':33133,'ィ':13,'ゥ':113,'ェ':31333,'ォ':13111})
signals.update({'ヵ':1311,'ヶ':3133,'ッ':1331})
signals.update({'パ':3111,'ピ':33113,'プ':3311,'ペ':1,'ポ':311})
signals.update({'ャ':133,'ュ':31133,'ョ':33,'ヮ':313})
signals.update({'Ａ':13,'Ｂ':3111,'Ｃ':3131,'Ｄ':311,'Ｅ':1,'Ｆ':1131,'Ｇ':331})
signals.update({'Ｈ':1111,'Ｉ':11,'Ｊ':1333,'Ｋ':313,'Ｌ':1311,'Ｍ':33,'Ｎ':31})
signals.update({'Ｏ':333,'Ｐ':1331,'Ｑ':3313,'Ｒ':131,'Ｓ':111,'Ｔ':3,'Ｕ':113})
signals.update({'Ｖ':1113,'Ｗ':133,'Ｘ':3113,'Ｙ':3133,'Ｚ':3311})
signals.update({'１':13333,'２':11333,'３':11133,'４':11113,'５':11111})
signals.update({'６':31111,'７':33111,'８':33311,'９':33331,'０':33333})

def _to_counts(kana):
	result = ""
	for c in kana:
		result += str(signals.get(c,"")) + "0"
	return result

def flash_signals(kana, span):
	AVCaptureDevice = ObjCClass('AVCaptureDevice')
	device = AVCaptureDevice.defaultDeviceWithMediaType_('vide')
	if not device.hasTorch():
		raise RuntimeError('Device has no flashlight')
	mode = device.torchMode()
	counts = _to_counts(kana)
	device.lockForConfiguration_(None)
	for s in counts:
		if int(s) != 0:
			device.setTorchMode_(1)
			time.sleep(int(s) * span)
		device.setTorchMode_(0)
		time.sleep(span)
	device.unlockForConfiguration()


