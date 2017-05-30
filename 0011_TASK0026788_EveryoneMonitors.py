import subaruwlst

def appendToRoleExpr(role, appendExpr):
        expr = rm.getRoleExpression(None,role)
        print "Current %s global role expression: %s" % (role, expr)
        if appendExpr in expr:
                print "Looks like new clause is already part of expression--skipping"
        else:
                expr = expr+appendExpr
                rm.setRoleExpression(None,role,expr)
                print "New %s global role expression: %s" % (role, expr)
        print


domCfg = subaruwlst.domainConfig()

connect(domCfg.adminUser(), domCfg.adminPass(), 't3://%s:%s' % (domCfg.servers[domCfg.adminServer]['listen_address'],domCfg.servers[domCfg.adminServer]['listen_port']))

serverConfig()

sr = cmo.getSecurityConfiguration().getDefaultRealm()
rm = sr.lookupRoleMapper('XACMLRoleMapper')
atnr=sr.lookupAuthenticationProvider('DefaultAuthenticator')

## Middleware-App-Developer
group = 'Middleware-App-Developer'
appendToRoleExpr('Monitor','|Grp('+group.replace('-', '#D')+')')
appendToRoleExpr('IntegrationMonitor','|Grp('+group.replace('-', '#D')+')')
grantAppRole('soa-infra','SOAMonitor','weblogic.security.principal.WLSGroupImpl',group)
grantAppRole('Service_Bus_Console','Monitor','weblogic.security.principal.WLSGroupImpl',group)

## Middleware-App-Deployer
group = 'Middleware-App-Deployer'
appendToRoleExpr('Monitor','|Grp('+group.replace('-', '#D')+')')
appendToRoleExpr('IntegrationMonitor','|Grp('+group.replace('-', '#D')+')')
grantAppRole('soa-infra','SOAMonitor','weblogic.security.principal.WLSGroupImpl',group)
grantAppRole('Service_Bus_Console','Monitor','weblogic.security.principal.WLSGroupImpl',group)

## Middleware-App-Operator
group = 'Middleware-App-Operator'
appendToRoleExpr('Monitor','|Grp('+group.replace('-', '#D')+')')
appendToRoleExpr('IntegrationMonitor','|Grp('+group.replace('-', '#D')+')')
grantAppRole('soa-infra','SOAMonitor','weblogic.security.principal.WLSGroupImpl',group)
grantAppRole('Service_Bus_Console','Monitor','weblogic.security.principal.WLSGroupImpl',group)

## Middleware-Operator
group = 'Middleware-Operator'
appendToRoleExpr('Monitor','|Grp('+group.replace('-', '#D')+')')
appendToRoleExpr('IntegrationMonitor','|Grp('+group.replace('-', '#D')+')')
grantAppRole('soa-infra','SOAMonitor','weblogic.security.principal.WLSGroupImpl',group)
grantAppRole('Service_Bus_Console','Monitor','weblogic.security.principal.WLSGroupImpl',group)




