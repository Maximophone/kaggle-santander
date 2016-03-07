import json

_settings_dict = json.load(open('./framework/settings.json','r'))

class Settings(object):
	def __init__(self,settings_dict):
		self._settings_dict = settings_dict
		for k,v in settings_dict.iteritems():
			setattr(self,k,Settings(v) if isinstance(v,dict) else v)

settings = Settings(_settings_dict)
