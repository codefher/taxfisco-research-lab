"""
TaxFisco custom Zeek script - detects fiscal-specific anomalies
"""

event connection_state_remove(c: connection)
{
    # Detect connections to administrative ports
    if (c$id$resp_p in set(22/tcp, 2222/tcp, 3389/tcp, 445/tcp, 23/tcp))
    {
        local info: TaxFisco::Info = [
            $ts=network_time(),
            $src_ip=c$id$orig_h,
            $src_port=c$id$orig_p,
            $dst_ip=c$id$resp_h,
            $dst_port=c$id$resp_p,
            $proto="tcp",
            $service="admin-service",
            $event_type="admin-access",
            $severity="MEDIUM",
            $description=fmt("Access to administrative service port %s", c$id$resp_p),
            $mitre_technique="T1078"
        ];
        TaxFisco::log_taxfisco_event(info);
    }
}
