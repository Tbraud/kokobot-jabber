import linkhandler as li
import quotehandler as qu

class CommandHandler(object):

    li=li.Link('articles')
    qu=qu.Quote('quotes')

    @classmethod
    def formatreturn(cls,msg,rv):
        return msg['mucnick']+": "+rv

    @classmethod
    def command(cls,msg):
        if "help" in msg['body']:
            return cls.show_help()
        #elif "http" in msg['body']:
        #    return cls.putlink(msg)
        elif "getlink" in msg['body']:
            return cls.getlink(msg)
        elif "getrandomlink" in msg['body']:
            return cls.getrandomlink(msg)
        elif "linkdbsize" in msg['body']:
            return cls.linkdbsize(msg)
        elif "searchlink" in msg['body']:
            return cls.searchlink(msg)
        elif "putquote" in msg['body']:
            return cls.putquote(msg)
        elif "getquote" in msg['body']:
            return cls.getquote(msg)
        elif "getrandomquote" in msg['body']:
            return cls.getrandomquote(msg)
        elif "quotedbsize" in msg['body']:
            return cls.quotedbsize(msg)
        elif "searchquote" in msg['body']:
            return cls.searchquote(msg)
        return cls.formatreturn(msg,"Je ne comprends pas")
    
    
    @classmethod
    def show_help(cls):
        rs="\n===== Kokobot - Documentation =====\n" \
                "--- Link management ---\n" \
                "Links on this room are automatically saved" \
                "* Kokobot getlink <index> -- Returns the link at <index>\n" \
                "* Kokobot getrandomlink   -- Returns a random link\n" \
                "* Kokobot linkdbsize      -- Returns the size of Kokobot's link database\n" \
                "* Kokobot searchlink <pattern> -- Returns links containing <pattern>\n" \
                "--- Wall of Fame ---\n" \
                "* Kokobot putquote <quote>  -- Put <quote> in Kokobot's database\n" \
                "* Kokobot getquote <index> -- Returns the quote at <index>\n" \
                "* Kokobot getrandomquote   -- Returns a random quote\n" \
                "* Kokobot quotedbsize      -- Returns the size of Kokobot's quote database\n" \
                "* Kokobot searchquote <pattern> -- Returns quotes containing <pattern>"
        return rs

    @classmethod
    def putlink(cls,msg):
        msg_list=msg['body'].split()
        for m in msg_list:
            if m.strip().startswith("https://") or m.strip().startswith("http://"):
                cls.li.process_link(m)

    @classmethod
    def getlink(cls,msg):
        index=int(msg['body'].split()[2])
        rv=cls.li.get_link_at(index)
        return cls.formatreturn(msg,rv)


    @classmethod
    def getrandomlink(cls,msg):
        rv=cls.li.get_random_link()
        return cls.formatreturn(msg,rv)

    @classmethod
    def linkdbsize(cls,msg):
        rv=str(cls.li.get_db_size())
        return cls.formatreturn(msg,rv)

    @classmethod
    def searchlink(cls,msg):
        pattern=msg['body'].split()[2]
        rv=cls.li.search_link(pattern)
        return cls.formatreturn(msg,rv)

    @classmethod
    def putquote(cls,msg):
        rv=cls.qu.save_quote(msg['body'].split(" ",2)[2].strip())
        return cls.formatreturn(msg,rv)

    @classmethod
    def getquote(cls,msg):
        index=int(msg['body'].split()[2])
        rv=cls.qu.get_quote_at(index)
        return cls.formatreturn(msg,rv)


    @classmethod
    def getrandomquote(cls,msg):
        rv=cls.qu.get_random_quote()
        return cls.formatreturn(msg,rv)

    @classmethod
    def quotedbsize(cls,msg):
        rv=str(cls.qu.get_db_size())
        return cls.formatreturn(msg,rv)

    @classmethod
    def searchquote(cls,msg):
        pattern=msg['body'].split()[2]
        rv=cls.qu.search_quote(pattern)
        return cls.formatreturn(msg,rv)
