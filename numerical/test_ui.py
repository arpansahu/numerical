"""
UI Tests for numerical calculator
Complete implementation of all calculator UI tests using Playwright.
"""
import pytest
from playwright.sync_api import Page, expect


@pytest.mark.ui
class TestHomeUI:
    """UI tests for calculator home page."""

    def test_home_page_loads(self, page: Page):
        """Test home page loads successfully."""
        page.goto("http://localhost:8000/")
        expect(page).to_have_title("NUMERICAL CALCULATOR")

    def test_calculator_display_visible(self, page: Page):
        """Test calculator display elements are visible."""
        page.goto("http://localhost:8000/")
        expect(page.locator("#equation-area")).to_be_visible()
        expect(page.locator("#result-area")).to_be_visible()

    # Number button tests
    def test_7(self, page: Page):
        """Test button: 7"""
        page.goto("http://localhost:8000/")
        button = page.locator('button[data-value="7"]')
        expect(button).to_be_visible()
        expect(button).to_be_enabled()

    def test_8(self, page: Page):
        """Test button: 8"""
        page.goto("http://localhost:8000/")
        button = page.locator('button[data-value="8"]')
        expect(button).to_be_visible()
        expect(button).to_be_enabled()

    def test_9(self, page: Page):
        """Test button: 9"""
        page.goto("http://localhost:8000/")
        button = page.locator('button[data-value="9"]')
        expect(button).to_be_visible()
        expect(button).to_be_enabled()

    def test_4(self, page: Page):
        """Test button: 4"""
        page.goto("http://localhost:8000/")
        button = page.locator('button[data-value="4"]')
        expect(button).to_be_visible()
        expect(button).to_be_enabled()

    def test_5(self, page: Page):
        """Test button: 5"""
        page.goto("http://localhost:8000/")
        button = page.locator('button[data-value="5"]')
        expect(button).to_be_visible()
        expect(button).to_be_enabled()

    def test_6(self, page: Page):
        """Test button: 6"""
        page.goto("http://localhost:8000/")
        button = page.locator('button[data-value="6"]')
        expect(button).to_be_visible()
        expect(button).to_be_enabled()

    def test_1(self, page: Page):
        """Test button: 1"""
        page.goto("http://localhost:8000/")
        button = page.locator('button[data-value="1"]')
        expect(button).to_be_visible()
        expect(button).to_be_enabled()

    def test_2(self, page: Page):
        """Test button: 2"""
        page.goto("http://localhost:8000/")
        button = page.locator('button[data-value="2"]')
        expect(button).to_be_visible()
        expect(button).to_be_enabled()

    def test_3(self, page: Page):
        """Test button: 3"""
        page.goto("http://localhost:8000/")
        button = page.locator('button[data-value="3"]')
        expect(button).to_be_visible()
        expect(button).to_be_enabled()

    def test_0(self, page: Page):
        """Test button: 0"""
        page.goto("http://localhost:8000/")
        button = page.locator('button[data-value="0"]')
        expect(button).to_be_visible()
        expect(button).to_be_enabled()

    # Operator button tests
    def test_unknown(self, page: Page):
        """Test button: ÷ (division)"""
        page.goto("http://localhost:8000/")
        button = page.locator('button[data-value="/"]')
        expect(button).to_be_visible()
        expect(button).to_be_enabled()

    def test_unknown_2(self, page: Page):
        """Test button: × (multiplication)"""
        page.goto("http://localhost:8000/")
        button = page.locator('button[data-value="*"]')
        expect(button).to_be_visible()
        expect(button).to_be_enabled()

    def test_unknown_4(self, page: Page):
        """Test button: − (subtraction)"""
        page.goto("http://localhost:8000/")
        button = page.locator('button[data-value="-"]')
        expect(button).to_be_visible()
        expect(button).to_be_enabled()

    def test_unknown_8(self, page: Page):
        """Test button: + (addition)"""
        page.goto("http://localhost:8000/")
        button = page.locator('button[data-value="+"]')
        expect(button).to_be_visible()
        expect(button).to_be_enabled()

    def test_unknown_5(self, page: Page):
        """Test button: ( (open parenthesis)"""
        page.goto("http://localhost:8000/")
        button = page.locator('button[data-value="("]')
        expect(button).to_be_visible()
        expect(button).to_be_enabled()

    def test_unknown_9(self, page: Page):
        """Test button: ) (close parenthesis)"""
        page.goto("http://localhost:8000/")
        button = page.locator('button[data-value=")"]')
        expect(button).to_be_visible()
        expect(button).to_be_enabled()

    def test_unknown_6(self, page: Page):
        """Test button: . (decimal point)"""
        page.goto("http://localhost:8000/")
        button = page.locator('button[data-value="."]')
        expect(button).to_be_visible()
        expect(button).to_be_enabled()

    def test_unknown_7(self, page: Page):
        """Test button: = (equals)"""
        page.goto("http://localhost:8000/")
        button = page.locator('button[data-value="="]')
        expect(button).to_be_visible()
        expect(button).to_be_enabled()

    # Function button tests
    def test_c(self, page: Page):
        """Test button: C (clear)"""
        page.goto("http://localhost:8000/")
        button = page.locator('button[data-action="clear"]')
        expect(button).to_be_visible()
        expect(button).to_be_enabled()

    def test_unknown_3(self, page: Page):
        """Test button: ⌫ (backspace)"""
        page.goto("http://localhost:8000/")
        button = page.locator('button[data-action="backspace"]')
        expect(button).to_be_visible()
        expect(button).to_be_enabled()

    def test_calculatebutton(self, page: Page):
        """Test calculate button"""
        page.goto("http://localhost:8000/")
        button = page.locator("#calculate-button")
        expect(button).to_be_visible()
        expect(button).to_be_enabled()

    # Modal tests
    def test_button(self, page: Page):
        """Test modal close button (btn-close)"""
        page.goto("http://localhost:8000/")
        # Modal close button exists in DOM but might not be visible initially
        # Just check it exists
        expect(page.locator(".btn-close")).to_have_count(1)

    def test_close(self, page: Page):
        """Test modal Close button"""
        page.goto("http://localhost:8000/")
        # Close button in modal exists but might not be visible
        # Just verify it's in the DOM
        close_buttons = page.locator('button.btn:has-text("Close")')
        expect(close_buttons).to_have_count(1)

