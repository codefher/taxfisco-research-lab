# Zeek local configuration for SIN Research Lab

@load base/frameworks/cluster
@load base/frameworks/logging
@load base/frameworks/notice

# Standard protocol logs
@load base/protocols/conn
@load base/protocols/http
@load base/protocols/dns
@load base/protocols/ssl
@load base/protocols/ssh
@load base/protocols/ftp
@load base/protocols/smb

# Detect sensitive activities (Zeek 6.0: some scripts moved/renamed)
@load policy/misc/scan
@load policy/misc/loaded-scripts
# Note: detect-bruteforcing / detect-unencrypted-passwords not available
# in this Zeek 6.0 image; bruteforce is detected via notice framework
# in sin-notice.zeek below.

# Custom scripts for SIN
@load /usr/local/zeek/share/zeek/site/sin-notice.zeek

# Tune defaults
redef ignore_checksums = T;
redef LogAscii::use_json = T;
