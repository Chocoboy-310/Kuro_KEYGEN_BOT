import dns.resolver
def get_real_ip(domain):
    try:
        answers = dns.resolver.resolve(domain, 'A')
        return answers[0].address
    except Exception as e:
        print(f"Error: {e}")
        return None

domain_to_resolve = "darkespyt.com"
real_ip = get_real_ip(domain_to_resolve)

if real_ip:
    print(f"The real IP address of {domain_to_resolve} is: {real_ip}")
