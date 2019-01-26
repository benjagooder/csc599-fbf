import sys
from antlr4 import *
from RomeParser import RomeParser
from RomeVisitor import RomeVisitor

class MercuryVisitor(RomeVisitor):

    def visitChildren(self, ctx:RomeParser.RomeContext):
        for c in ctx.getChildren():
            self.visit(c)

    def visit(self, ctx):
        if isinstance(ctx, RomeParser.RomeContext):
            return self.visitRome(ctx)
        elif isinstance(ctx, RomeParser.LineContext):
            return self.visitLine(ctx)
    
    # rome: line+ EOF ;
    def visitRome(self, ctx:RomeParser.RomeContext):
        return self.visitChildren(ctx)
    
    def getNumberOfMessages(self, ctx:RomeParser.RomeContext):
        return len(ctx.line())

    # rome: line+ EOF ;
    def getLinks(self, ctx:RomeParser.RomeContext):
        links = {}
        
        for line in ctx.line():
            link = self.visitLine(line)                        
            if isinstance(link, tuple):
                if link[0] in links.keys():
                    links[link[0]] += link[1]
                else:
                    links[link[0]] = link[1]            

        return links

    # BENJAS TOMFOOLERY #####################################
    # rome: line+ EOF ;
    def getMessages(self, ctx:RomeParser.RomeContext):
        rMessages = {}
        possibleGold = []

        #rThisMessage = self.visitMessage(ctx.message())
        for line in ctx.line():
            rThisMessage = self.romeVisitLine(line)
            #print(rThisMessage)


            possibleGold.append(rThisMessage)




            #if isinstance(rThisMessage, tuple):
            #    if rThisMessage[0] in rMessages.keys():
            #        rMessages[rThisMessage[0]] += rThisMessage[1]
            #    else:
            #        rMessages[rThisMessage[0]] = rThisMessage[1]

        #return rMessages
        return possibleGold

    # line: name command message NEWLINE ;
    def romeVisitLine(self, ctx:RomeParser.LineContext):
        #print("romeVisitLine")

        #isolatedEntry = []  #delete me

        rMessages = self.romeVisitMessage(ctx.message())

        if rMessages is not None:
            rMessages = (ctx.name().getText(), rMessages)

        return rMessages

    # message: (emoticon | link | color | mention | WORD)+ ;
    def romeVisitMessage(self, ctx: RomeParser.MessageContext):
        rMessages = []
        # Check WORD
        if len(ctx.WORD()) > 0:
            for word in ctx.WORD():
                #print(word.getText())
                rMessages.append(word.getText())

        return rMessages if len(rMessages) > 0 else None

    #########################################################
                    
    # line: name command message NEWLINE ;
    def visitLine(self, ctx:RomeParser.LineContext):

        #print("visitLine")
        links = self.visitMessage(ctx.message())

        if links is not None:
            links = (ctx.name().getText(), links)

        return links                   
        
    # message: (emoticon | link | color | mention | WORD)+ ;
    def visitMessage(self, ctx:RomeParser.MessageContext):
        links = []
        
        # color : '/' WORD '/' message '/';
        if len(ctx.color()) > 0 :
            for color in ctx.color():
                #print(color.getText())
                link = self.visitMessage(color.message())
                if isinstance(link, list):
                    links = links + link

        # link: TEXT '(' URL ')' ;
        # this code extracts only URL part
        if len(ctx.link()) > 0 :
            for link in ctx.link():
                links.append(link.URL().getText())

        # Check WORD
        #if len(ctx.WORD()) > 0:
        #    for word in ctx.WORD():
        #        print(word.getText())

        return links if len(links) > 0 else None

