FROM wazuh/wazuh-indexer:4.10.4

# Switch to root to modify system files
USER root

# Create necessary directories
RUN mkdir -p /etc/wazuh-indexer/certs
RUN mkdir -p /var/log/wazuh-indexer
RUN mkdir -p /var/lib/wazuh-indexer
RUN mkdir -p /usr/share/wazuh-indexer/opensearch-performance-analyzer/

# Copy custom config (SSL habilitado con certs)
COPY opensearch.yml /etc/wazuh-indexer/opensearch.yml
COPY opensearch_security.policy /usr/share/wazuh-indexer/opensearch-performance-analyzer/opensearch_security.policy

# Set proper permissions for the wazuh-indexer user
RUN chown -R wazuh-indexer:wazuh-indexer /etc/wazuh-indexer
RUN chown -R wazuh-indexer:wazuh-indexer /var/log/wazuh-indexer
RUN chown -R wazuh-indexer:wazuh-indexer /var/lib/wazuh-indexer

# Switch back to the wazuh-indexer user
USER wazuh-indexer
