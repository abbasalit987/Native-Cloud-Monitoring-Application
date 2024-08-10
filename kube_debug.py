from kubernetes import config

# Print the list of contexts in the kubeconfig file
contexts, active_context = config.list_kube_config_contexts()
print("Available contexts:")
for context in contexts:
    print(context['name'])

print("\nActive context:")
print(active_context)
