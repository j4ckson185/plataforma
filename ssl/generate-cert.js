const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const sslDir = path.join(__dirname);

try {
    // Verificar se o OpenSSL está disponível
    execSync('openssl version', { stdio: 'ignore' });

    // Comandos para gerar as chaves e o certificado autoassinado
    const genKeyCmd = `openssl genrsa -out ${path.join(sslDir, 'localhost-key.pem')} 2048`;
    const genCertCmd = `openssl req -new -x509 -key ${path.join(sslDir, 'localhost-key.pem')} -out ${path.join(sslDir, 'localhost.pem')} -days 365 -subj "/CN=localhost"`;

    // Executar os comandos
    execSync(genKeyCmd);
    execSync(genCertCmd);

    console.log('Certificados gerados com sucesso!');
} catch (error) {
    console.error('Erro ao gerar certificados:', error);
}
