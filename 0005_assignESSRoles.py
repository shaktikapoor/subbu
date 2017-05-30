import subaruwlst

domCfg = subaruwlst.domainConfig()

connect(domCfg.adminUser(), domCfg.adminPass(), 't3://%s:%s' % (domCfg.servers[domCfg.adminServer]['listen_address'],domCfg.servers[domCfg.adminServer]['listen_port']))

serverConfig()

sr = cmo.getSecurityConfiguration().getDefaultRealm()
rm = sr.lookupRoleMapper('XACMLRoleMapper')
atnr=sr.lookupAuthenticationProvider('DefaultAuthenticator')

## Middleware-Admin
group = 'Middleware-Admin'
grantAppRole('ESSAPP','ESSAdmin','weblogic.security.principal.WLSGroupImpl',group)
grantAppRole('ESSAPP','ESSAuditAdmin','weblogic.security.principal.WLSGroupImpl',group)
grantAppRole('ESSAPP','ESSAuditViewer','weblogic.security.principal.WLSGroupImpl',group)

## Middleware-App-Developer
group = 'Middleware-App-Developer'
grantAppRole('ESSAPP','ESSOperator','weblogic.security.principal.WLSGroupImpl',group)

## Middleware-App-Deployer
group = 'Middleware-App-Deployer'
grantAppRole('ESSAPP','ESSAdmin','weblogic.security.principal.WLSGroupImpl',group)

## Middleware-App-Operator
group = 'Middleware-App-Operator'
grantAppRole('ESSAPP','ESSOperator','weblogic.security.principal.WLSGroupImpl',group)

## Middleware-Monitor
group = 'Middleware-Monitor'
grantAppRole('ESSAPP','ESSMonitor','weblogic.security.principal.WLSGroupImpl',group)

## Middleware-Operator
group = 'Middleware-Operator'
grantAppRole('ESSAPP','ESSOperator','weblogic.security.principal.WLSGroupImpl',group)

