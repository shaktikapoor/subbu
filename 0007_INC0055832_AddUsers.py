import subaruwlst
from passwd import mkpasswd

domCfg = subaruwlst.domainConfig()

connect(domCfg.adminUser(), domCfg.adminPass(), 't3://%s:%s' % (domCfg.servers[domCfg.adminServer]['listen_address'],domCfg.servers[domCfg.adminServer]['listen_port']))

serverConfig()

sr = cmo.getSecurityConfiguration().getDefaultRealm()
rm = sr.lookupRoleMapper('XACMLRoleMapper')
atnr=sr.lookupAuthenticationProvider('DefaultAuthenticator')

userlist = [
'vxliqskal',
'vxliqnpul',
'vxsvemu',
'vxliqkgun',
'vxliqvlak'
]

for X in userlist:
  user, passwd = X, mkpasswd()
  try:
    atnr.createUser(user, passwd, user)
    atnr.addMemberToGroup('Middleware-Monitor',user)
    print "%s	%s" % (user, passwd)
  except:
    print "Could not create %s" % (user)
    pass

