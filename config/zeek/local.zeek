# Zeek local configuration for TaxFisco Research Lab

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
@load base/protocols/sip
@load base/protocols/dhcp
@load base/protocols/notice

# Detect sensitive activities
@load base/frameworks/notice
@load policy/misc/detect-bruteforcing
@load policy/misc/detect-port-scan
@load policy/misc/detect-unencrypted-passwords
@load policy/misc/detect-suspicious

# Custom scripts for TaxFisco
@load /usr/local/zeek/share/zeek/site/taxfisco-notice.zeek

# Tune defaults
redef ignore_checksums = T;
redef LogAscii::use_json = T;
redef Notice::emailed_events = "";

# Capture all output as JSON for ingestion into Wazuh
@load base/protocols/conn
redef Log::default_writer = Log::WRITER_ASCII;
redef Log::default_rotation_interval = 1 hr;
redef Log::default_rotation_postprocessor = "";

event zeek_init()
{
    Log::create_stream(TaxFisco::LOG, [$columns=TaxFisco::Info, $ev=TaxFisco::log_taxfisco_event]);
}

module TaxFisco;

export {
    type Info: record {
        ts: time &log;
        src_ip: addr &log;
        src_port: port &log;
        dst_ip: addr &log;
        dst_port: port &log;
        proto: string &log;
        service: string &log;
        event_type: string &log;
        severity: string &log;
        description: string &log;
        mitre_technique: string &log;
    };
}

event log_taxfisco_event(info: TaxFisco::Info)
{
    Log::write(TaxFisco::LOG, info);
}
