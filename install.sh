#!/usr/bin/env bash
set -e

SCRIPT_NAME="pymini"
SOURCE_DIR="$(pwd)"
INSTALL_DIR="$HOME/.local/share/$SCRIPT_NAME"
BIN_PATH="$HOME/.local/bin/$SCRIPT_NAME"

# Make sure target dirs exist
mkdir -p "$INSTALL_DIR"
mkdir -p "$(dirname "$BIN_PATH")"

# Copy full source
echo "[INFO] Copying source files to $INSTALL_DIR..."
cp -r "$SOURCE_DIR"/* "$INSTALL_DIR"

# Create a wrapper executable
echo "[INFO] Creating launch script at $BIN_PATH..."
cat > "$BIN_PATH" <<EOF
#!/usr/bin/env bash
python3 "$INSTALL_DIR/main.py" "\$@"
EOF

chmod +x "$BIN_PATH"

# Ensure ~/.local/bin is in PATH
SHELL_RC="$HOME/.bashrc"
[ -n "$ZSH_VERSION" ] && SHELL_RC="$HOME/.zshrc"

if ! echo "$PATH" | grep -q "$HOME/.local/bin"; then
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$SHELL_RC"
    echo "[INFO] Added ~/.local/bin to PATH in $SHELL_RC"
    echo "[INFO] Please run: source $SHELL_RC"
fi

echo "[SUCCESS] Installed pymini. Run it with: $SCRIPT_NAME"
