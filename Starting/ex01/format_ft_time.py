from datetime import datetime

d = datetime.now()
t = d.timestamp()

print(
    """
    Seconds since January 1, 1970: {:,} or {:.2e} in scientific notation
    """.format(t, t)
    )
print(d.strftime("%Y-%m-%d"))
