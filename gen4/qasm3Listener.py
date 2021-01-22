# Generated from qasm3.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .qasm3Parser import qasm3Parser
else:
    from qasm3Parser import qasm3Parser

# This class defines a complete listener for a parse tree produced by qasm3Parser.
class qasm3Listener(ParseTreeListener):

    # Enter a parse tree produced by qasm3Parser#program.
    def enterProgram(self, ctx:qasm3Parser.ProgramContext):
        pass

    # Exit a parse tree produced by qasm3Parser#program.
    def exitProgram(self, ctx:qasm3Parser.ProgramContext):
        pass


    # Enter a parse tree produced by qasm3Parser#header.
    def enterHeader(self, ctx:qasm3Parser.HeaderContext):
        pass

    # Exit a parse tree produced by qasm3Parser#header.
    def exitHeader(self, ctx:qasm3Parser.HeaderContext):
        pass


    # Enter a parse tree produced by qasm3Parser#version.
    def enterVersion(self, ctx:qasm3Parser.VersionContext):
        pass

    # Exit a parse tree produced by qasm3Parser#version.
    def exitVersion(self, ctx:qasm3Parser.VersionContext):
        pass


    # Enter a parse tree produced by qasm3Parser#include.
    def enterInclude(self, ctx:qasm3Parser.IncludeContext):
        pass

    # Exit a parse tree produced by qasm3Parser#include.
    def exitInclude(self, ctx:qasm3Parser.IncludeContext):
        pass


    # Enter a parse tree produced by qasm3Parser#globalStatement.
    def enterGlobalStatement(self, ctx:qasm3Parser.GlobalStatementContext):
        pass

    # Exit a parse tree produced by qasm3Parser#globalStatement.
    def exitGlobalStatement(self, ctx:qasm3Parser.GlobalStatementContext):
        pass


    # Enter a parse tree produced by qasm3Parser#statement.
    def enterStatement(self, ctx:qasm3Parser.StatementContext):
        pass

    # Exit a parse tree produced by qasm3Parser#statement.
    def exitStatement(self, ctx:qasm3Parser.StatementContext):
        pass


    # Enter a parse tree produced by qasm3Parser#quantumDeclarationStatement.
    def enterQuantumDeclarationStatement(self, ctx:qasm3Parser.QuantumDeclarationStatementContext):
        pass

    # Exit a parse tree produced by qasm3Parser#quantumDeclarationStatement.
    def exitQuantumDeclarationStatement(self, ctx:qasm3Parser.QuantumDeclarationStatementContext):
        pass


    # Enter a parse tree produced by qasm3Parser#classicalDeclarationStatement.
    def enterClassicalDeclarationStatement(self, ctx:qasm3Parser.ClassicalDeclarationStatementContext):
        pass

    # Exit a parse tree produced by qasm3Parser#classicalDeclarationStatement.
    def exitClassicalDeclarationStatement(self, ctx:qasm3Parser.ClassicalDeclarationStatementContext):
        pass


    # Enter a parse tree produced by qasm3Parser#classicalAssignment.
    def enterClassicalAssignment(self, ctx:qasm3Parser.ClassicalAssignmentContext):
        pass

    # Exit a parse tree produced by qasm3Parser#classicalAssignment.
    def exitClassicalAssignment(self, ctx:qasm3Parser.ClassicalAssignmentContext):
        pass


    # Enter a parse tree produced by qasm3Parser#assignmentStatement.
    def enterAssignmentStatement(self, ctx:qasm3Parser.AssignmentStatementContext):
        pass

    # Exit a parse tree produced by qasm3Parser#assignmentStatement.
    def exitAssignmentStatement(self, ctx:qasm3Parser.AssignmentStatementContext):
        pass


    # Enter a parse tree produced by qasm3Parser#returnSignature.
    def enterReturnSignature(self, ctx:qasm3Parser.ReturnSignatureContext):
        pass

    # Exit a parse tree produced by qasm3Parser#returnSignature.
    def exitReturnSignature(self, ctx:qasm3Parser.ReturnSignatureContext):
        pass


    # Enter a parse tree produced by qasm3Parser#designator.
    def enterDesignator(self, ctx:qasm3Parser.DesignatorContext):
        pass

    # Exit a parse tree produced by qasm3Parser#designator.
    def exitDesignator(self, ctx:qasm3Parser.DesignatorContext):
        pass


    # Enter a parse tree produced by qasm3Parser#doubleDesignator.
    def enterDoubleDesignator(self, ctx:qasm3Parser.DoubleDesignatorContext):
        pass

    # Exit a parse tree produced by qasm3Parser#doubleDesignator.
    def exitDoubleDesignator(self, ctx:qasm3Parser.DoubleDesignatorContext):
        pass


    # Enter a parse tree produced by qasm3Parser#identifierList.
    def enterIdentifierList(self, ctx:qasm3Parser.IdentifierListContext):
        pass

    # Exit a parse tree produced by qasm3Parser#identifierList.
    def exitIdentifierList(self, ctx:qasm3Parser.IdentifierListContext):
        pass


    # Enter a parse tree produced by qasm3Parser#association.
    def enterAssociation(self, ctx:qasm3Parser.AssociationContext):
        pass

    # Exit a parse tree produced by qasm3Parser#association.
    def exitAssociation(self, ctx:qasm3Parser.AssociationContext):
        pass


    # Enter a parse tree produced by qasm3Parser#quantumType.
    def enterQuantumType(self, ctx:qasm3Parser.QuantumTypeContext):
        pass

    # Exit a parse tree produced by qasm3Parser#quantumType.
    def exitQuantumType(self, ctx:qasm3Parser.QuantumTypeContext):
        pass


    # Enter a parse tree produced by qasm3Parser#quantumDeclaration.
    def enterQuantumDeclaration(self, ctx:qasm3Parser.QuantumDeclarationContext):
        pass

    # Exit a parse tree produced by qasm3Parser#quantumDeclaration.
    def exitQuantumDeclaration(self, ctx:qasm3Parser.QuantumDeclarationContext):
        pass


    # Enter a parse tree produced by qasm3Parser#quantumArgument.
    def enterQuantumArgument(self, ctx:qasm3Parser.QuantumArgumentContext):
        pass

    # Exit a parse tree produced by qasm3Parser#quantumArgument.
    def exitQuantumArgument(self, ctx:qasm3Parser.QuantumArgumentContext):
        pass


    # Enter a parse tree produced by qasm3Parser#quantumArgumentList.
    def enterQuantumArgumentList(self, ctx:qasm3Parser.QuantumArgumentListContext):
        pass

    # Exit a parse tree produced by qasm3Parser#quantumArgumentList.
    def exitQuantumArgumentList(self, ctx:qasm3Parser.QuantumArgumentListContext):
        pass


    # Enter a parse tree produced by qasm3Parser#bitType.
    def enterBitType(self, ctx:qasm3Parser.BitTypeContext):
        pass

    # Exit a parse tree produced by qasm3Parser#bitType.
    def exitBitType(self, ctx:qasm3Parser.BitTypeContext):
        pass


    # Enter a parse tree produced by qasm3Parser#singleDesignatorType.
    def enterSingleDesignatorType(self, ctx:qasm3Parser.SingleDesignatorTypeContext):
        pass

    # Exit a parse tree produced by qasm3Parser#singleDesignatorType.
    def exitSingleDesignatorType(self, ctx:qasm3Parser.SingleDesignatorTypeContext):
        pass


    # Enter a parse tree produced by qasm3Parser#doubleDesignatorType.
    def enterDoubleDesignatorType(self, ctx:qasm3Parser.DoubleDesignatorTypeContext):
        pass

    # Exit a parse tree produced by qasm3Parser#doubleDesignatorType.
    def exitDoubleDesignatorType(self, ctx:qasm3Parser.DoubleDesignatorTypeContext):
        pass


    # Enter a parse tree produced by qasm3Parser#noDesignatorType.
    def enterNoDesignatorType(self, ctx:qasm3Parser.NoDesignatorTypeContext):
        pass

    # Exit a parse tree produced by qasm3Parser#noDesignatorType.
    def exitNoDesignatorType(self, ctx:qasm3Parser.NoDesignatorTypeContext):
        pass


    # Enter a parse tree produced by qasm3Parser#classicalType.
    def enterClassicalType(self, ctx:qasm3Parser.ClassicalTypeContext):
        pass

    # Exit a parse tree produced by qasm3Parser#classicalType.
    def exitClassicalType(self, ctx:qasm3Parser.ClassicalTypeContext):
        pass


    # Enter a parse tree produced by qasm3Parser#constantDeclaration.
    def enterConstantDeclaration(self, ctx:qasm3Parser.ConstantDeclarationContext):
        pass

    # Exit a parse tree produced by qasm3Parser#constantDeclaration.
    def exitConstantDeclaration(self, ctx:qasm3Parser.ConstantDeclarationContext):
        pass


    # Enter a parse tree produced by qasm3Parser#singleDesignatorDeclaration.
    def enterSingleDesignatorDeclaration(self, ctx:qasm3Parser.SingleDesignatorDeclarationContext):
        pass

    # Exit a parse tree produced by qasm3Parser#singleDesignatorDeclaration.
    def exitSingleDesignatorDeclaration(self, ctx:qasm3Parser.SingleDesignatorDeclarationContext):
        pass


    # Enter a parse tree produced by qasm3Parser#doubleDesignatorDeclaration.
    def enterDoubleDesignatorDeclaration(self, ctx:qasm3Parser.DoubleDesignatorDeclarationContext):
        pass

    # Exit a parse tree produced by qasm3Parser#doubleDesignatorDeclaration.
    def exitDoubleDesignatorDeclaration(self, ctx:qasm3Parser.DoubleDesignatorDeclarationContext):
        pass


    # Enter a parse tree produced by qasm3Parser#noDesignatorDeclaration.
    def enterNoDesignatorDeclaration(self, ctx:qasm3Parser.NoDesignatorDeclarationContext):
        pass

    # Exit a parse tree produced by qasm3Parser#noDesignatorDeclaration.
    def exitNoDesignatorDeclaration(self, ctx:qasm3Parser.NoDesignatorDeclarationContext):
        pass


    # Enter a parse tree produced by qasm3Parser#bitDeclaration.
    def enterBitDeclaration(self, ctx:qasm3Parser.BitDeclarationContext):
        pass

    # Exit a parse tree produced by qasm3Parser#bitDeclaration.
    def exitBitDeclaration(self, ctx:qasm3Parser.BitDeclarationContext):
        pass


    # Enter a parse tree produced by qasm3Parser#classicalDeclaration.
    def enterClassicalDeclaration(self, ctx:qasm3Parser.ClassicalDeclarationContext):
        pass

    # Exit a parse tree produced by qasm3Parser#classicalDeclaration.
    def exitClassicalDeclaration(self, ctx:qasm3Parser.ClassicalDeclarationContext):
        pass


    # Enter a parse tree produced by qasm3Parser#classicalTypeList.
    def enterClassicalTypeList(self, ctx:qasm3Parser.ClassicalTypeListContext):
        pass

    # Exit a parse tree produced by qasm3Parser#classicalTypeList.
    def exitClassicalTypeList(self, ctx:qasm3Parser.ClassicalTypeListContext):
        pass


    # Enter a parse tree produced by qasm3Parser#classicalArgument.
    def enterClassicalArgument(self, ctx:qasm3Parser.ClassicalArgumentContext):
        pass

    # Exit a parse tree produced by qasm3Parser#classicalArgument.
    def exitClassicalArgument(self, ctx:qasm3Parser.ClassicalArgumentContext):
        pass


    # Enter a parse tree produced by qasm3Parser#classicalArgumentList.
    def enterClassicalArgumentList(self, ctx:qasm3Parser.ClassicalArgumentListContext):
        pass

    # Exit a parse tree produced by qasm3Parser#classicalArgumentList.
    def exitClassicalArgumentList(self, ctx:qasm3Parser.ClassicalArgumentListContext):
        pass


    # Enter a parse tree produced by qasm3Parser#aliasStatement.
    def enterAliasStatement(self, ctx:qasm3Parser.AliasStatementContext):
        pass

    # Exit a parse tree produced by qasm3Parser#aliasStatement.
    def exitAliasStatement(self, ctx:qasm3Parser.AliasStatementContext):
        pass


    # Enter a parse tree produced by qasm3Parser#indexIdentifier.
    def enterIndexIdentifier(self, ctx:qasm3Parser.IndexIdentifierContext):
        pass

    # Exit a parse tree produced by qasm3Parser#indexIdentifier.
    def exitIndexIdentifier(self, ctx:qasm3Parser.IndexIdentifierContext):
        pass


    # Enter a parse tree produced by qasm3Parser#indexIdentifierList.
    def enterIndexIdentifierList(self, ctx:qasm3Parser.IndexIdentifierListContext):
        pass

    # Exit a parse tree produced by qasm3Parser#indexIdentifierList.
    def exitIndexIdentifierList(self, ctx:qasm3Parser.IndexIdentifierListContext):
        pass


    # Enter a parse tree produced by qasm3Parser#indexEqualsAssignmentList.
    def enterIndexEqualsAssignmentList(self, ctx:qasm3Parser.IndexEqualsAssignmentListContext):
        pass

    # Exit a parse tree produced by qasm3Parser#indexEqualsAssignmentList.
    def exitIndexEqualsAssignmentList(self, ctx:qasm3Parser.IndexEqualsAssignmentListContext):
        pass


    # Enter a parse tree produced by qasm3Parser#rangeDefinition.
    def enterRangeDefinition(self, ctx:qasm3Parser.RangeDefinitionContext):
        pass

    # Exit a parse tree produced by qasm3Parser#rangeDefinition.
    def exitRangeDefinition(self, ctx:qasm3Parser.RangeDefinitionContext):
        pass


    # Enter a parse tree produced by qasm3Parser#quantumGateDefinition.
    def enterQuantumGateDefinition(self, ctx:qasm3Parser.QuantumGateDefinitionContext):
        pass

    # Exit a parse tree produced by qasm3Parser#quantumGateDefinition.
    def exitQuantumGateDefinition(self, ctx:qasm3Parser.QuantumGateDefinitionContext):
        pass


    # Enter a parse tree produced by qasm3Parser#quantumGateSignature.
    def enterQuantumGateSignature(self, ctx:qasm3Parser.QuantumGateSignatureContext):
        pass

    # Exit a parse tree produced by qasm3Parser#quantumGateSignature.
    def exitQuantumGateSignature(self, ctx:qasm3Parser.QuantumGateSignatureContext):
        pass


    # Enter a parse tree produced by qasm3Parser#quantumBlock.
    def enterQuantumBlock(self, ctx:qasm3Parser.QuantumBlockContext):
        pass

    # Exit a parse tree produced by qasm3Parser#quantumBlock.
    def exitQuantumBlock(self, ctx:qasm3Parser.QuantumBlockContext):
        pass


    # Enter a parse tree produced by qasm3Parser#quantumLoop.
    def enterQuantumLoop(self, ctx:qasm3Parser.QuantumLoopContext):
        pass

    # Exit a parse tree produced by qasm3Parser#quantumLoop.
    def exitQuantumLoop(self, ctx:qasm3Parser.QuantumLoopContext):
        pass


    # Enter a parse tree produced by qasm3Parser#quantumLoopBlock.
    def enterQuantumLoopBlock(self, ctx:qasm3Parser.QuantumLoopBlockContext):
        pass

    # Exit a parse tree produced by qasm3Parser#quantumLoopBlock.
    def exitQuantumLoopBlock(self, ctx:qasm3Parser.QuantumLoopBlockContext):
        pass


    # Enter a parse tree produced by qasm3Parser#quantumStatement.
    def enterQuantumStatement(self, ctx:qasm3Parser.QuantumStatementContext):
        pass

    # Exit a parse tree produced by qasm3Parser#quantumStatement.
    def exitQuantumStatement(self, ctx:qasm3Parser.QuantumStatementContext):
        pass


    # Enter a parse tree produced by qasm3Parser#quantumInstruction.
    def enterQuantumInstruction(self, ctx:qasm3Parser.QuantumInstructionContext):
        pass

    # Exit a parse tree produced by qasm3Parser#quantumInstruction.
    def exitQuantumInstruction(self, ctx:qasm3Parser.QuantumInstructionContext):
        pass


    # Enter a parse tree produced by qasm3Parser#quantumPhase.
    def enterQuantumPhase(self, ctx:qasm3Parser.QuantumPhaseContext):
        pass

    # Exit a parse tree produced by qasm3Parser#quantumPhase.
    def exitQuantumPhase(self, ctx:qasm3Parser.QuantumPhaseContext):
        pass


    # Enter a parse tree produced by qasm3Parser#quantumMeasurement.
    def enterQuantumMeasurement(self, ctx:qasm3Parser.QuantumMeasurementContext):
        pass

    # Exit a parse tree produced by qasm3Parser#quantumMeasurement.
    def exitQuantumMeasurement(self, ctx:qasm3Parser.QuantumMeasurementContext):
        pass


    # Enter a parse tree produced by qasm3Parser#quantumMeasurementAssignment.
    def enterQuantumMeasurementAssignment(self, ctx:qasm3Parser.QuantumMeasurementAssignmentContext):
        pass

    # Exit a parse tree produced by qasm3Parser#quantumMeasurementAssignment.
    def exitQuantumMeasurementAssignment(self, ctx:qasm3Parser.QuantumMeasurementAssignmentContext):
        pass


    # Enter a parse tree produced by qasm3Parser#quantumBarrier.
    def enterQuantumBarrier(self, ctx:qasm3Parser.QuantumBarrierContext):
        pass

    # Exit a parse tree produced by qasm3Parser#quantumBarrier.
    def exitQuantumBarrier(self, ctx:qasm3Parser.QuantumBarrierContext):
        pass


    # Enter a parse tree produced by qasm3Parser#quantumGateModifier.
    def enterQuantumGateModifier(self, ctx:qasm3Parser.QuantumGateModifierContext):
        pass

    # Exit a parse tree produced by qasm3Parser#quantumGateModifier.
    def exitQuantumGateModifier(self, ctx:qasm3Parser.QuantumGateModifierContext):
        pass


    # Enter a parse tree produced by qasm3Parser#quantumGateCall.
    def enterQuantumGateCall(self, ctx:qasm3Parser.QuantumGateCallContext):
        pass

    # Exit a parse tree produced by qasm3Parser#quantumGateCall.
    def exitQuantumGateCall(self, ctx:qasm3Parser.QuantumGateCallContext):
        pass


    # Enter a parse tree produced by qasm3Parser#quantumGateName.
    def enterQuantumGateName(self, ctx:qasm3Parser.QuantumGateNameContext):
        pass

    # Exit a parse tree produced by qasm3Parser#quantumGateName.
    def exitQuantumGateName(self, ctx:qasm3Parser.QuantumGateNameContext):
        pass


    # Enter a parse tree produced by qasm3Parser#unaryOperator.
    def enterUnaryOperator(self, ctx:qasm3Parser.UnaryOperatorContext):
        pass

    # Exit a parse tree produced by qasm3Parser#unaryOperator.
    def exitUnaryOperator(self, ctx:qasm3Parser.UnaryOperatorContext):
        pass


    # Enter a parse tree produced by qasm3Parser#binaryOperator.
    def enterBinaryOperator(self, ctx:qasm3Parser.BinaryOperatorContext):
        pass

    # Exit a parse tree produced by qasm3Parser#binaryOperator.
    def exitBinaryOperator(self, ctx:qasm3Parser.BinaryOperatorContext):
        pass


    # Enter a parse tree produced by qasm3Parser#expressionStatement.
    def enterExpressionStatement(self, ctx:qasm3Parser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by qasm3Parser#expressionStatement.
    def exitExpressionStatement(self, ctx:qasm3Parser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by qasm3Parser#expression.
    def enterExpression(self, ctx:qasm3Parser.ExpressionContext):
        pass

    # Exit a parse tree produced by qasm3Parser#expression.
    def exitExpression(self, ctx:qasm3Parser.ExpressionContext):
        pass


    # Enter a parse tree produced by qasm3Parser#expressionTerminator.
    def enterExpressionTerminator(self, ctx:qasm3Parser.ExpressionTerminatorContext):
        pass

    # Exit a parse tree produced by qasm3Parser#expressionTerminator.
    def exitExpressionTerminator(self, ctx:qasm3Parser.ExpressionTerminatorContext):
        pass


    # Enter a parse tree produced by qasm3Parser#expressionList.
    def enterExpressionList(self, ctx:qasm3Parser.ExpressionListContext):
        pass

    # Exit a parse tree produced by qasm3Parser#expressionList.
    def exitExpressionList(self, ctx:qasm3Parser.ExpressionListContext):
        pass


    # Enter a parse tree produced by qasm3Parser#builtInCall.
    def enterBuiltInCall(self, ctx:qasm3Parser.BuiltInCallContext):
        pass

    # Exit a parse tree produced by qasm3Parser#builtInCall.
    def exitBuiltInCall(self, ctx:qasm3Parser.BuiltInCallContext):
        pass


    # Enter a parse tree produced by qasm3Parser#builtInMath.
    def enterBuiltInMath(self, ctx:qasm3Parser.BuiltInMathContext):
        pass

    # Exit a parse tree produced by qasm3Parser#builtInMath.
    def exitBuiltInMath(self, ctx:qasm3Parser.BuiltInMathContext):
        pass


    # Enter a parse tree produced by qasm3Parser#castOperator.
    def enterCastOperator(self, ctx:qasm3Parser.CastOperatorContext):
        pass

    # Exit a parse tree produced by qasm3Parser#castOperator.
    def exitCastOperator(self, ctx:qasm3Parser.CastOperatorContext):
        pass


    # Enter a parse tree produced by qasm3Parser#incrementor.
    def enterIncrementor(self, ctx:qasm3Parser.IncrementorContext):
        pass

    # Exit a parse tree produced by qasm3Parser#incrementor.
    def exitIncrementor(self, ctx:qasm3Parser.IncrementorContext):
        pass


    # Enter a parse tree produced by qasm3Parser#equalsExpression.
    def enterEqualsExpression(self, ctx:qasm3Parser.EqualsExpressionContext):
        pass

    # Exit a parse tree produced by qasm3Parser#equalsExpression.
    def exitEqualsExpression(self, ctx:qasm3Parser.EqualsExpressionContext):
        pass


    # Enter a parse tree produced by qasm3Parser#assignmentOperator.
    def enterAssignmentOperator(self, ctx:qasm3Parser.AssignmentOperatorContext):
        pass

    # Exit a parse tree produced by qasm3Parser#assignmentOperator.
    def exitAssignmentOperator(self, ctx:qasm3Parser.AssignmentOperatorContext):
        pass


    # Enter a parse tree produced by qasm3Parser#equalsAssignmentList.
    def enterEqualsAssignmentList(self, ctx:qasm3Parser.EqualsAssignmentListContext):
        pass

    # Exit a parse tree produced by qasm3Parser#equalsAssignmentList.
    def exitEqualsAssignmentList(self, ctx:qasm3Parser.EqualsAssignmentListContext):
        pass


    # Enter a parse tree produced by qasm3Parser#membershipTest.
    def enterMembershipTest(self, ctx:qasm3Parser.MembershipTestContext):
        pass

    # Exit a parse tree produced by qasm3Parser#membershipTest.
    def exitMembershipTest(self, ctx:qasm3Parser.MembershipTestContext):
        pass


    # Enter a parse tree produced by qasm3Parser#setDeclaration.
    def enterSetDeclaration(self, ctx:qasm3Parser.SetDeclarationContext):
        pass

    # Exit a parse tree produced by qasm3Parser#setDeclaration.
    def exitSetDeclaration(self, ctx:qasm3Parser.SetDeclarationContext):
        pass


    # Enter a parse tree produced by qasm3Parser#programBlock.
    def enterProgramBlock(self, ctx:qasm3Parser.ProgramBlockContext):
        pass

    # Exit a parse tree produced by qasm3Parser#programBlock.
    def exitProgramBlock(self, ctx:qasm3Parser.ProgramBlockContext):
        pass


    # Enter a parse tree produced by qasm3Parser#branchingStatement.
    def enterBranchingStatement(self, ctx:qasm3Parser.BranchingStatementContext):
        pass

    # Exit a parse tree produced by qasm3Parser#branchingStatement.
    def exitBranchingStatement(self, ctx:qasm3Parser.BranchingStatementContext):
        pass


    # Enter a parse tree produced by qasm3Parser#loopSignature.
    def enterLoopSignature(self, ctx:qasm3Parser.LoopSignatureContext):
        pass

    # Exit a parse tree produced by qasm3Parser#loopSignature.
    def exitLoopSignature(self, ctx:qasm3Parser.LoopSignatureContext):
        pass


    # Enter a parse tree produced by qasm3Parser#loopStatement.
    def enterLoopStatement(self, ctx:qasm3Parser.LoopStatementContext):
        pass

    # Exit a parse tree produced by qasm3Parser#loopStatement.
    def exitLoopStatement(self, ctx:qasm3Parser.LoopStatementContext):
        pass


    # Enter a parse tree produced by qasm3Parser#controlDirectiveStatement.
    def enterControlDirectiveStatement(self, ctx:qasm3Parser.ControlDirectiveStatementContext):
        pass

    # Exit a parse tree produced by qasm3Parser#controlDirectiveStatement.
    def exitControlDirectiveStatement(self, ctx:qasm3Parser.ControlDirectiveStatementContext):
        pass


    # Enter a parse tree produced by qasm3Parser#controlDirective.
    def enterControlDirective(self, ctx:qasm3Parser.ControlDirectiveContext):
        pass

    # Exit a parse tree produced by qasm3Parser#controlDirective.
    def exitControlDirective(self, ctx:qasm3Parser.ControlDirectiveContext):
        pass


    # Enter a parse tree produced by qasm3Parser#kernelDeclaration.
    def enterKernelDeclaration(self, ctx:qasm3Parser.KernelDeclarationContext):
        pass

    # Exit a parse tree produced by qasm3Parser#kernelDeclaration.
    def exitKernelDeclaration(self, ctx:qasm3Parser.KernelDeclarationContext):
        pass


    # Enter a parse tree produced by qasm3Parser#kernelCall.
    def enterKernelCall(self, ctx:qasm3Parser.KernelCallContext):
        pass

    # Exit a parse tree produced by qasm3Parser#kernelCall.
    def exitKernelCall(self, ctx:qasm3Parser.KernelCallContext):
        pass


    # Enter a parse tree produced by qasm3Parser#subroutineDefinition.
    def enterSubroutineDefinition(self, ctx:qasm3Parser.SubroutineDefinitionContext):
        pass

    # Exit a parse tree produced by qasm3Parser#subroutineDefinition.
    def exitSubroutineDefinition(self, ctx:qasm3Parser.SubroutineDefinitionContext):
        pass


    # Enter a parse tree produced by qasm3Parser#returnStatement.
    def enterReturnStatement(self, ctx:qasm3Parser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by qasm3Parser#returnStatement.
    def exitReturnStatement(self, ctx:qasm3Parser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by qasm3Parser#subroutineBlock.
    def enterSubroutineBlock(self, ctx:qasm3Parser.SubroutineBlockContext):
        pass

    # Exit a parse tree produced by qasm3Parser#subroutineBlock.
    def exitSubroutineBlock(self, ctx:qasm3Parser.SubroutineBlockContext):
        pass


    # Enter a parse tree produced by qasm3Parser#subroutineCall.
    def enterSubroutineCall(self, ctx:qasm3Parser.SubroutineCallContext):
        pass

    # Exit a parse tree produced by qasm3Parser#subroutineCall.
    def exitSubroutineCall(self, ctx:qasm3Parser.SubroutineCallContext):
        pass


    # Enter a parse tree produced by qasm3Parser#pragma.
    def enterPragma(self, ctx:qasm3Parser.PragmaContext):
        pass

    # Exit a parse tree produced by qasm3Parser#pragma.
    def exitPragma(self, ctx:qasm3Parser.PragmaContext):
        pass


    # Enter a parse tree produced by qasm3Parser#timingType.
    def enterTimingType(self, ctx:qasm3Parser.TimingTypeContext):
        pass

    # Exit a parse tree produced by qasm3Parser#timingType.
    def exitTimingType(self, ctx:qasm3Parser.TimingTypeContext):
        pass


    # Enter a parse tree produced by qasm3Parser#timingBox.
    def enterTimingBox(self, ctx:qasm3Parser.TimingBoxContext):
        pass

    # Exit a parse tree produced by qasm3Parser#timingBox.
    def exitTimingBox(self, ctx:qasm3Parser.TimingBoxContext):
        pass


    # Enter a parse tree produced by qasm3Parser#timingTerminator.
    def enterTimingTerminator(self, ctx:qasm3Parser.TimingTerminatorContext):
        pass

    # Exit a parse tree produced by qasm3Parser#timingTerminator.
    def exitTimingTerminator(self, ctx:qasm3Parser.TimingTerminatorContext):
        pass


    # Enter a parse tree produced by qasm3Parser#timingIdentifier.
    def enterTimingIdentifier(self, ctx:qasm3Parser.TimingIdentifierContext):
        pass

    # Exit a parse tree produced by qasm3Parser#timingIdentifier.
    def exitTimingIdentifier(self, ctx:qasm3Parser.TimingIdentifierContext):
        pass


    # Enter a parse tree produced by qasm3Parser#timingInstructionName.
    def enterTimingInstructionName(self, ctx:qasm3Parser.TimingInstructionNameContext):
        pass

    # Exit a parse tree produced by qasm3Parser#timingInstructionName.
    def exitTimingInstructionName(self, ctx:qasm3Parser.TimingInstructionNameContext):
        pass


    # Enter a parse tree produced by qasm3Parser#timingInstruction.
    def enterTimingInstruction(self, ctx:qasm3Parser.TimingInstructionContext):
        pass

    # Exit a parse tree produced by qasm3Parser#timingInstruction.
    def exitTimingInstruction(self, ctx:qasm3Parser.TimingInstructionContext):
        pass


    # Enter a parse tree produced by qasm3Parser#timingStatement.
    def enterTimingStatement(self, ctx:qasm3Parser.TimingStatementContext):
        pass

    # Exit a parse tree produced by qasm3Parser#timingStatement.
    def exitTimingStatement(self, ctx:qasm3Parser.TimingStatementContext):
        pass


    # Enter a parse tree produced by qasm3Parser#calibration.
    def enterCalibration(self, ctx:qasm3Parser.CalibrationContext):
        pass

    # Exit a parse tree produced by qasm3Parser#calibration.
    def exitCalibration(self, ctx:qasm3Parser.CalibrationContext):
        pass


    # Enter a parse tree produced by qasm3Parser#calibrationGrammarDeclaration.
    def enterCalibrationGrammarDeclaration(self, ctx:qasm3Parser.CalibrationGrammarDeclarationContext):
        pass

    # Exit a parse tree produced by qasm3Parser#calibrationGrammarDeclaration.
    def exitCalibrationGrammarDeclaration(self, ctx:qasm3Parser.CalibrationGrammarDeclarationContext):
        pass


    # Enter a parse tree produced by qasm3Parser#calibrationDefinition.
    def enterCalibrationDefinition(self, ctx:qasm3Parser.CalibrationDefinitionContext):
        pass

    # Exit a parse tree produced by qasm3Parser#calibrationDefinition.
    def exitCalibrationDefinition(self, ctx:qasm3Parser.CalibrationDefinitionContext):
        pass


    # Enter a parse tree produced by qasm3Parser#calibrationGrammar.
    def enterCalibrationGrammar(self, ctx:qasm3Parser.CalibrationGrammarContext):
        pass

    # Exit a parse tree produced by qasm3Parser#calibrationGrammar.
    def exitCalibrationGrammar(self, ctx:qasm3Parser.CalibrationGrammarContext):
        pass


    # Enter a parse tree produced by qasm3Parser#calibrationArgumentList.
    def enterCalibrationArgumentList(self, ctx:qasm3Parser.CalibrationArgumentListContext):
        pass

    # Exit a parse tree produced by qasm3Parser#calibrationArgumentList.
    def exitCalibrationArgumentList(self, ctx:qasm3Parser.CalibrationArgumentListContext):
        pass



del qasm3Parser