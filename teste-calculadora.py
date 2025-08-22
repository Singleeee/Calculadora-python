import pytest
from io import StringIO
import sys
from unittest.mock import patch

# Importar a função calculadora (assumindo que está em um arquivo chamado calculadora.py)
from calculadora import calculadora

def test_adicao():
    """Testa operação de adição"""
    with patch('builtins.input', side_effect=['1', '5', '3']):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            calculadora()
            output = mock_stdout.getvalue()
            assert "Resultado: 8.0" in output

def test_subtracao():
    """Testa operação de subtração"""
    with patch('builtins.input', side_effect=['2', '10', '4']):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            calculadora()
            output = mock_stdout.getvalue()
            assert "Resultado: 6.0" in output

def test_multiplicacao():
    """Testa operação de multiplicação"""
    with patch('builtins.input', side_effect=['3', '7', '6']):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            calculadora()
            output = mock_stdout.getvalue()
            assert "Resultado: 42.0" in output

def test_divisao():
    """Testa operação de divisão"""
    with patch('builtins.input', side_effect=['4', '15', '3']):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            calculadora()
            output = mock_stdout.getvalue()
            assert "Resultado: 5.0" in output

def test_divisao_por_zero():
    """Testa divisão por zero"""
    with patch('builtins.input', side_effect=['4', '10', '0']):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            calculadora()
            output = mock_stdout.getvalue()
            assert "Erro: Divisão por zero" in output

def test_exponencial():
    """Testa operação exponencial"""
    with patch('builtins.input', side_effect=['6', '2', '3']):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            calculadora()
            output = mock_stdout.getvalue()
            assert "Resultado: 8.0" in output

def test_operacao_invalida():
    """Testa operação inválida"""
    with patch('builtins.input', side_effect=['99', '2', '3']):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            calculadora()
            output = mock_stdout.getvalue()
            assert "Operação inválida" in output

def test_entrada_invalida():
    """Testa entrada de valores não numéricos"""
    with patch('builtins.input', side_effect=['1', 'abc', '3']):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            calculadora()
            output = mock_stdout.getvalue()
            assert "Entrada inválida" in output

def test_logaritmo_valores_positivos():
    """Testa logaritmo com valores positivos"""
    with patch('builtins.input', side_effect=['5', '100', '10']):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            calculadora()
            output = mock_stdout.getvalue()
            # O log10(100)/log10(10) = 2/1 = 2
            assert "Resultado: 2.0" in output

def test_logaritmo_valor_negativo():
    """Testa logaritmo com valores negativos"""
    with patch('builtins.input', side_effect=['5', '-10', '2']):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            calculadora()
            output = mock_stdout.getvalue()
            assert "Erro: Logaritmo apenas para valores positivos" in output

def test_logaritmo_zero():
    """Testa logaritmo com zero"""
    with patch('builtins.input', side_effect=['5', '0', '2']):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            calculadora()
            output = mock_stdout.getvalue()
            assert "Erro: Logaritmo apenas para valores positivos" in output

def test_fluxo_completo():
    """Testa o fluxo completo com múltiplas operações"""
    test_cases = [
        (['1', '5', '3'], "Resultado: 8.0"),
        (['2', '10', '4'], "Resultado: 6.0"),
        (['3', '7', '6'], "Resultado: 42.0"),
        (['4', '15', '3'], "Resultado: 5.0"),
    ]
    
    for inputs, expected_output in test_cases:
        with patch('builtins.input', side_effect=inputs):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                calculadora()
                output = mock_stdout.getvalue()
                assert expected_output in output