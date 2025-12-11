class MCPHandlers:
    def format_realtime(self, data):
        return {"type": "realtime", "data": data}

    def format_historical(self, data):
        return {"type": "historical", "data": data}

mcp_handlers = MCPHandlers()
