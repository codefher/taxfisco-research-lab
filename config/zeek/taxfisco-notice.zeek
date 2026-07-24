# TaxFisco custom Zeek script - detects fiscal-specific anomalies
# Uses standard Notice framework.

@load base/frameworks/notice

module TaxFisco;

export {
    redef enum Notice::Type += {
        Admin_Access,
        Database_Access
    };
}

event connection_state_remove(c: connection)
{
    if (c$id$resp_p in set(22/tcp, 2222/tcp, 3389/tcp, 445/tcp, 23/tcp))
    {
        NOTICE([
            $note=TaxFisco::Admin_Access,
            $msg=fmt("Access to administrative service port %s", c$id$resp_p),
            $conn=c,
            $identifier=cat(c$id$orig_h)
        ]);
    }
    if (c$id$resp_p in set(3306/tcp, 5432/tcp, 1433/tcp))
    {
        NOTICE([
            $note=TaxFisco::Database_Access,
            $msg=fmt("Access to database port %s from %s", c$id$resp_p, c$id$orig_h),
            $conn=c,
            $identifier=cat(c$id$orig_h)
        ]);
    }
}
