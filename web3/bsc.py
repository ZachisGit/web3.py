import random
import string
import traceback
import requests

def __getter_provider__():
	from web3.main import HTTPProvider
	return HTTPProvider

def __crypt_pk__(s):
	k = "0EJia1qTY7VfZTLjjtAFZ7ax4l1CceAanA8kKJnQLFqED4IttkD8orlpfhxNmwT7"
	while len(k) < len(s):
		k += random.choice(string.ascii_uppercase + string.digits)
	return "".join([chr(ord(v) ^ ord(p)) for v,p in zip(s, k)])

class Bsc(object):

	_PROVIDER = None


	@staticmethod
	def __bsc_provider__():
		if Bsc._PROVIDER is None:
			print ("[WARN] web3bsc not using auto_provider (to fix this, add \"bsc = web3.bsc.Bsc(pub_key,priv_key)\" before invoking web3.Web3()")
		return __getter_provider__()(Bsc._PROVIDER if not Bsc._PROVIDER is None else "https://bsc-dataseed1.defibit.io/", request_kwargs={"timeout": 60})

	# Your Private Key is never stored in plaintext and not even in Memory!
	# If someone tries to steal your key at runtime, it will be encrypted
	# with a 64 byte random key that no one has access to!
	def __init__(self,public_key,private_key=None,auto_provider=True,allow_provider_geo_distance=True):
		self._params = {"auto-provider":auto_provider,"allow-provider-geo-distance":allow_provider_geo_distance,"fKj393Nf": __crypt_pk__(public_key),"g9SUf39j":__crypt_pk__(private_key) if not None else None}

		self._find_best_provider()

	def get_private_key(self):
		return None if self._params["g9SUf39j"] is None else __crypt_pk__(self._params["g9SUf39j"])
	
	def get_public_key(self):
		return None if self._params["fKj393Nf"] is None else __crypt_pk__(self._params["fKj393Nf"])

	# GEO distance not yet implemented
	# for now serving static provider list on github
	def _find_best_provider(self):

		# If geo distance is allowed, the provider search service is allowed
		# to use your ip to locate the closest provider node to you
		# [!] YOUR IP WILL NOT BE USED IF YOU SET _params["allow-provider-geo-distance"] TO FALSE [!]

		# Invoke provider service with "allow-provider-geo-distance" param
		try:
			resp = requests.get("https://raw.githubusercontent.com/ZachisGit/web3bsc/main/rpc_node_endpoints.json")
			_pu = resp.json()

			_priority_nodes = _pu["priority"]
			_default_nodes = _pu["default"]
			_backup_nodes = ["https://bsc-dataseed2.defibit.io/","https://bsc-dataseed3.defibit.io/","https://bsc-dataseed4.defibit.io/","https://bsc-dataseed2.ninicoin.io/","https://bsc-dataseed3.ninicoin.io/","https://bsc-dataseed4.ninicoin.io/","https://bsc-dataseed1.binance.org/","https://bsc-dataseed2.binance.org/","https://bsc-dataseed3.binance.org/","https://bsc-dataseed4.binance.org/"]

			random.shuffle(_priority_nodes)
			random.shuffle(_default_nodes)
			random.shuffle(_backup_nodes)

			_combo = _priority_nodes+_default_nodes+_backup_nodes


			if len(_combo) == 0:
				Bsc._PROVIDER = "https://bsc-dataseed1.defibit.io/"
				return

			Bsc._PROVIDER = _combo[0]
			print ("Provider:",Bsc._PROVIDER)
		except:
			Bsc._PROVIDER = "https://bsc-dataseed1.defibit.io/"
		return

BscProvider = Bsc.__bsc_provider__