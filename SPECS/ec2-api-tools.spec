Name:           ec2-api-tools
Version:        1.6.12.0
Release:        1%{?dist}
Summary:        Amazon EC2 Command-Line Tools

Group:          Applications/Internet
License:        Redistributable, no modification permitted and LGPLv2 and ASL 2.0 and ASL 1.1 
# Just to avoid confusion, "ASL" above is Apache Software License
# "Redistributable" parts are covered by Amazon Software License
URL:            http://developer.amazonwebservices.com/connect/entry.jspa?externalID=351
Source0:        http://s3.amazonaws.com/ec2-downloads/%{name}.zip

Source1:        ec2-cmd
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%if 0%{?fedora} < 20
Requires:       javapackages-tools
%else
Requires:       jpackage-utils
%endif
Requires:       java >= 1.5
Requires:       apache-commons-cli 
Requires:       commons-codec 
Requires:       apache-commons-discovery 
Requires:       commons-httpclient 
Requires:       apache-commons-logging
Requires:       bcprov 
Requires:       bea-stax-api 
Requires:       javamail 
Requires:       jdom 
Requires:       log4j 
Requires:       wsdl4j 
Requires:       xalan-j2 

BuildArch:      noarch

%description
The command-line tools serve as the client interface to the Amazon EC2 web
service. Use these tools to register and launch instances, manipulate
security groups, and more.


%prep
%setup -q -n %{name}-%{version}


%build
# Drop jars that are distributable by Fedora
xargs rm -f <<EOF
lib/activation-1.1.jar
lib/bcprov.jar
lib/commons-cli-1.1.jar
lib/commons-codec-1.3.jar
lib/commons-discovery-0.2.jar
lib/commons-httpclient-3.0.jar
lib/commons-logging-1.0.4.jar
lib/jaxb-api-2.0.jar
lib/jdom-1.0.jar
lib/log4j.jar
lib/mail-1.4.jar
lib/stax-api-1.0.1.jar
lib/wsdl4j-1.6.1.jar
lib/xalan-j2-2.7.0.jar
lib/xalan-j2-serializer-2.7.0.jar
EOF


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}/ec2-api-tools
install -pm 644 lib/*.jar $RPM_BUILD_ROOT%{_javadir}/ec2-api-tools

install -d $RPM_BUILD_ROOT%{_bindir}

# Rewrite the wrappers
for FILE in $(ls bin/* |grep -v 'cmd$')
do
        TARGET=$RPM_BUILD_ROOT%{_bindir}/$(basename $FILE)
        METHOD=$(awk '/ec2-cmd/ {printf "%s", $2}' $FILE)

cat >$TARGET <<EOF
#!/bin/bash
exec ec2-cmd $METHOD "\$@"
EOF

        chmod 0755 $TARGET
        touch --reference $FILE $TARGET
done

# The bundled ec2-cmd is not suitable for us
install -pm 755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/ec2-cmd


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_javadir}/ec2-api-tools
%doc THIRDPARTYLICENSE.TXT license.txt notice.txt


%changelog
* Fri Dec 20 2013 Julian Dunn <jdunn@aquezada.com> - 1.6.12.0-1
- Upgrade to 1.6.12.0
- Remove dep on jpackage-utils

* Wed Jul 03 2013 Julian Dunn <jdunn@aquezada.com> - 1.6.7.4-1
- Upgrade to 1.6.7.4

* Tue Jan 15 2013 Julian Dunn <jdunn@aquezada.com> - 1.6.6.0-1
- Upgrade to 1.6.6.0

* Thu Sep 20 2012 Julian Dunn <jdunn@aquezada.com> - 1.6.3.0-1
- Upgrade to 1.6.3.0

* Mon Aug 06 2012 Julian Dunn <jdunn@aquezada.com> - 1.6.1.2-1
- Upgrade to 1.6.1.2, to support new Amazon Elastic Block Store (EBS)
  volume type: Provisioned IOPS (input/output operations per second)
  and the ability to launch selected Amazon EC2 instance types as
  EBS-Optimized instances.

* Sat May 12 2012 Julian Dunn <jdunn@aquezada.com> - 1.5.3.1-1
- Upgrade to 1.5.3.1, including support for AWS Marketplace.

* Fri Mar 23 2012 Julian Dunn <jdunn@aquezada.com> - 1.5.2.5-1
- Bump version

* Wed May 18 2011 Julian Dunn <jdunn@aquezada.com> - 1.4.2.4-1
- Rebuilt for new versioning from Amazon
- Removed dependency on certain JARs that are already in any modern
  JVM runtime

* Wed Feb 23 2011 Julian Dunn <jdunn@aquezada.com> - 1.3.62308-1
- Rebuilt for 62308, VM import

* Thu Nov 04 2010 Julian Dunn <jdunn@aquezada.com> - 1.3.57419-1
- Rebuilt for 57419, Tagging, Filtering, Import Key Pair, and Idempotency.

* Sat Aug 21 2010 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 1.3.53907-3
- rebuilt

* Mon Aug 09 2010 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> - 1.3.53907-2
- Reuse distribution JARs wherever possible

* Mon Aug 09 2010 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> - 1.3.53907-1
- Update to 53907, support for Cluster Compute instances

* Fri Dec 18 2009 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> - 1.3.46266-1
- Update to 46266

* Wed Jul 15 2009 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> - 1.3.36506-1
- Bump to newer upstream version
- Publising, remove profanity
- Don't depend on Sun Java specifically

* Thu Dec 11 2008 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> - 1.3.30349-1
- New upstream release, support for European zones

* Tue Oct 7 2008 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> - 1.3.24159-2
- Require Sun Java

* Tue Oct 7 2008 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> - 1.3.24159-1
- Initial packaging attempt
