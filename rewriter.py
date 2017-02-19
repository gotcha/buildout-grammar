from BuildoutVisitor import BuildoutVisitor


class RewriteVisitor(BuildoutVisitor):

    def visitChildren(self, node):
        if node.getChildCount() == 0:
            result = node.getText()
            if result == '<EOF>':
                return ''
            else:
                return result
        else:
            result = list()
            for child in node.getChildren():
               result.append(self.visitChildren(child))
            return "".join(result)
