from src import parser

def test_parse_syslog():
    assert isinstance(parser.parse_syslog("data/sample_syslog.log"), list)
