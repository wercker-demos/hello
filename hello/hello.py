import argparse

from bottle import Bottle, run, request

app = Bottle()


@app.route('/')
def hello():

    # This will be true if launched as a test
    if "args" not in globals():
        message = "TEST MESSAGE"
    else:
        message_f = open(args.messagefile, "r")
        message = message_f.read()

    return message


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Serve a hello message over HTTP.")

    parser.add_argument('hostname', default="0.0.0.0",
                        help='The host IP to listen on. ')

    parser.add_argument('port', default="8080", help='The port to listen on.')
    parser.add_argument(
        'messagefile', help='A file that contains the message to display'
    )

    args = parser.parse_args()

    run(app, host=args.hostname, port=args.port)
