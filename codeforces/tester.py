import sys
import subprocess
from rich.console import Console
from rich.table import Table
from rich import box
from rich.text import Text
from rich.prompt import Prompt


def run_and_capture(script_path, input_lines):
    try:
        # Run the script with provided input
        result = subprocess.run(
            [sys.executable, script_path],
            input="\n".join(input_lines) + "\n",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        if result.stderr:
            return result.stdout.splitlines(), result.stderr.strip()
        return result.stdout.splitlines(), None
    except Exception as e:
        return [], str(e)


def read_lines(prompt_title):
    console = Console()
    console.print(f"\n[bold cyan]> {prompt_title} (end with empty line):[/]\n")
    lines = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        if not line.strip():
            break
        lines.append(line.strip())
    return lines


def compare_outputs(res, expected, err=None):
    console = Console()
    table = Table(
        title="[bold underline green]Test Case Comparison[/]",
        show_header=True,
        header_style="bold white on dark_green",
        box=box.ROUNDED,
        show_lines=True,
        padding=(0, 1),
    )

    table.add_column("Index", justify="center", style="bold yellow", width=8)
    table.add_column("Your Output", style="cyan", overflow="fold", justify="left")
    table.add_column("Expected Output", style="green", overflow="fold", justify="left")
    table.add_column("Status", justify="center", width=10)

    max_len = max(len(res), len(expected))

    passed = failed = 0
    for i in range(max_len):
        r = res[i] if i < len(res) else "[dim]<missing>[/dim]"
        e = expected[i] if i < len(expected) else "[dim]<missing>[/dim]"

        if r == e:
            status = Text("✅ PASS", style="bold green")
            passed += 1
        else:
            status = Text("❌ FAIL", style="bold red")
            failed += 1

        table.add_row(str(i), r, e, status)

    console.print("\n")
    console.print(table)

    console.print(
        f"\n[bold cyan]Summary:[/] [green]✓ {passed} passed[/], [red]✗ {failed} failed[/]\n"
    )

    if err:
        console.print("[bold red]Script Error Output:[/]")
        console.print(f"[dim]{err}[/]\n")


def main():
    if len(sys.argv) != 2:
        print("Usage: python tester.py <script.py>")
        sys.exit(1)

    script_path = sys.argv[1]

    input_lines = read_lines("Enter input")
    expected_output = read_lines("Enter expected output")

    actual_output, stderr = run_and_capture(script_path, input_lines)

    compare_outputs(actual_output, expected_output, err=stderr)


if __name__ == "__main__":
    main()

