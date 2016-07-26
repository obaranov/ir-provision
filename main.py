from infrared.core import api


def main():
    spec = api.create_spec(
        api.InfraredConfig.from_ini_file('provisioner', 'infrared.cfg'))
    if spec:
        spec.run()

if __name__ == '__main__':
    main()
