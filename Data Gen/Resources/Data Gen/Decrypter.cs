public static AesManaged GetAes(string key)
        {
            AesManaged myAes = new AesManaged();
            myAes.Padding = PaddingMode.PKCS7;
            myAes.Mode = CipherMode.ECB;
            byte[] keyBytes = new byte[16];
            if (key.Length == 16)
            {
                Array.Copy(Encoding.ASCII.GetBytes(key), keyBytes, 16);
            }
            else if (key.Length == 15)
            {
                Array.Copy(Encoding.ASCII.GetBytes(key), keyBytes, 15);
            }
            else
            {
                Array.Copy(Encoding.ASCII.GetBytes(key), keyBytes, 8);
            }
            myAes.Key = keyBytes;
            return myAes;
        }
        public static string DecryptData2(string data, string key)
        {
            AesManaged myAes = GetAes(key);
            ICryptoTransform decryptor = myAes.CreateDecryptor(myAes.Key, new byte[16]);
            using (MemoryStream stream = new MemoryStream(Convert.FromBase64String(data)))
            {
                using (CryptoStream csEncrypt = new CryptoStream(stream, decryptor, CryptoStreamMode.Read))
                {
                    using (TextReader reader = new StreamReader(csEncrypt))
                    {
                        return reader.ReadToEnd();
                    }
                }
            }
            return "";
        }
