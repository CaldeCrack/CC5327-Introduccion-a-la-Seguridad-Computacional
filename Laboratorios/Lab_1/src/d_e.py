import utils

CONNECTION_ADDR_A = ("cc5327.hackerlab.cl", 5312)
CONNECTION_ADDR_B = ("cc5327.hackerlab.cl", 5313)

if __name__ == "__main__":
    sock_input_A, sock_output_A = utils.create_socket(CONNECTION_ADDR_A)
    sock_input_B, sock_output_B = utils.create_socket(CONNECTION_ADDR_B)

    while True:
        try:
            response: str = input("send a message: ")
            print("[Client] \"{}\"".format(response))
            cipher_text: str = utils.send_message(sock_input_A, sock_output_A, response)
            print("[Server] \"{}\"".format(cipher_text))

            split_resp: list[bytearray] = utils.split_blocks(utils.hex_to_bytes(cipher_text), 16)
            plaintext_result: list[list[int]] = []
            for block_index in range(len(split_resp) - 1, 0, -1):
                print(f"\n--- Bloque {block_index} ---")
                c_i: bytearray = split_resp[block_index]
                c_i_1: bytearray = bytearray(split_resp[block_index - 1])

                intermediate: list[int] = [0] * 16
                recovered_plaintext: list[int] = [0] * 16
                for pad in range(1, 17):
                    print(f"\nByte con padding 0x{pad:02x}")

                    for guess in range(256):
                        mod_block: bytearray = c_i_1.copy()
                        for i in range(1, pad):
                            mod_block[-i] = intermediate[-i] ^ pad

                        mod_block[-pad] = guess
                        crafted_cipher: list[bytearray] = split_resp[:block_index - 1] + [mod_block, c_i]
                        crafted_hex: str = utils.bytes_to_hex(utils.join_blocks(crafted_cipher))
                        result: str = utils.send_message(sock_input_B, sock_output_B, crafted_hex)
                        
                        if 'invalid padding' not in result:
                            intermediate_value: int = guess ^ pad
                            intermediate[-pad] = intermediate_value
                            recovered_plaintext[-pad] = intermediate_value ^ c_i_1[-pad]
                            print(f"- Byte encontrado: {recovered_plaintext[-pad]:02x} ({chr(recovered_plaintext[-pad])})")
                            break

                plaintext_result.insert(0, recovered_plaintext)

            flat_bytes = bytearray()
            for block in plaintext_result:
                flat_bytes.extend(block)
            print(f"\nTexto plano recuperado: {flat_bytes.decode()}")

        except Exception as e:
            print(e)
            print("Closing...")
            break

