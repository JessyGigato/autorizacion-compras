from django.contrib.auth.backends import ModelBackend
from autorizacion_compras.domain_config import AUTH_INFORMATION
from django.contrib.auth.models import User
from django.utils import timezone
try:
    from ldap3 import Server, Connection, STRATEGY_SYNC, NTLM, ALL, ALL_ATTRIBUTES, SUBTREE
    from ldap3.core.exceptions import LDAPInvalidCredentialsResult
except ImportError:
    pass


LDAP_INFORMATION = AUTH_INFORMATION['LDAP']

class LDAPBackend(ModelBackend):
    def __init__(self,*args, **kwargs):
        super(LDAPBackend, self).__init__(*args, **kwargs)
        try:
            self.ldap_server = Server(host=LDAP_INFORMATION['HOST'],port=LDAP_INFORMATION['PORT'])
        except Exception as Error:
            pass

    def authenticate(self, username=None, password=None, **kwargs):
        domain_name = LDAP_INFORMATION['DOMAIN']
        username = domain_name + '\\' + username

        try:
            connection = Connection(self.ldap_server,user=username,password=password)
            connection.open()
        except Exception as e:
            pass
        
        is_connected = connection.bind()

        if is_connected:
            if User.objects.filter(username__exact=username).exists():
                user = User.objects.get(username__exact=username)
                user.last_login = timezone.now()
                user.save()
                return user
            else:
                return None
        
        return None
        