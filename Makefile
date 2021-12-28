OBS_PROJECT := EA4
scl-php72-php-ioncube10-obs : DISABLE_BUILD += repository=xUbuntu_20.04
scl-php71-php-ioncube10-obs : DISABLE_BUILD += repository=CentOS_8 repository=xUbuntu_20.04
scl-php70-php-ioncube10-obs : DISABLE_BUILD += repository=CentOS_8 repository=xUbuntu_20.04
scl-php56-php-ioncube10-obs : DISABLE_BUILD += repository=CentOS_8 repository=xUbuntu_20.04
scl-php55-php-ioncube10-obs : DISABLE_BUILD += repository=CentOS_8 repository=xUbuntu_20.04
scl-php54-php-ioncube10-obs : DISABLE_BUILD += repository=CentOS_8 repository=xUbuntu_20.04
OBS_PACKAGE := scl-ioncube10
include $(EATOOLS_BUILD_DIR)obs-scl.mk
