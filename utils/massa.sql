-- Limpeza inicial das tabelas (opcional - descomente se necessário)
-- TRUNCATE TABLE public.item CASCADE;
-- TRUNCATE TABLE public.todo_list CASCADE;
-- TRUNCATE TABLE public."user" CASCADE;

-- Inserção de usuários com senhas hashadas
-- As senhas foram hashadas com bcrypt (custo 12)
INSERT INTO public.usuario (user_id, nome_usuario, email, senha, data_criacao) VALUES
(1, 'johndoe', 'secret', '$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW', '2023-01-15 09:30:00'),
(2, 'maria_admin', 'maria@admin.com', '$2a$12$8Hj3Vp6N2sA7fL5qR9dW.uKv7XyZ1wC3bRn4tS5yV6mB8n9D0E1F2', '2023-02-20 14:15:00'),
(3, 'carlos_user', 'carlos@user.com', '$2a$12$3Mk5P7q9R1sT2V4X6Y8Z.A0B1C2D3E4F5G6H7I8J9K0L1M2N3O4P', '2023-03-10 10:00:00'),
(4, 'ana_tech', 'ana@tech.com', '$2a$12$2L4N6P8R0T1V3X5Z7Y9A.B1C3D5E7F9G1H2J3K4L5M6N7O8P9Q0', '2023-04-05 16:45:00'),
(5, 'pedro_devops', 'pedro@devops.com', '$2a$12$1Q3S5U7W9Y1B3D5F7H9J.K2L4N6P8R0T2V4X6Z8A0B1C3D5E7F9', '2023-05-12 11:20:00');

-- Inserção de todo_lists
INSERT INTO public.todo_list (todo_list_id, user_id, titulo, data_criacao) VALUES
(1, 1, 'Tarefas de Desenvolvimento', '2023-01-16 08:00:00'),
(2, 1, 'Compras do Mês', '2023-01-18 10:30:00'),
(3, 2, 'Tarefas Administrativas', '2023-02-21 09:15:00'),
(4, 3, 'Estudos de Programação', '2023-03-11 14:00:00'),
(5, 4, 'Projetos de TI', '2023-04-06 17:30:00'),
(6, 5, 'Configurações DevOps', '2023-05-13 12:45:00');

-- Inserção de itens
INSERT INTO public.item (item_id, todo_list_id, titulo, descricao, concluido) VALUES
-- Itens para a lista "Tarefas de Desenvolvimento" (user 1)
(1, 1, 'API REST', 'Implementar endpoints da API', false),
(2, 1, 'Testes Unitários', 'Escrever testes para módulo de autenticação', true),
(3, 1, 'Documentação', 'Atualizar documentação Swagger', false),

-- Itens para a lista "Compras do Mês" (user 1)
(4, 2, 'Alimentos', 'Comprar frutas e verduras', true),
(5, 2, 'Material de Escritório', 'Cadernos e canetas', false),
(6, 2, 'Eletrônicos', 'Cabos USB e adaptadores', false),

-- Itens para a lista "Tarefas Administrativas" (user 2)
(7, 3, 'Relatório Mensal', 'Preparar relatório de desempenho', false),
(8, 3, 'Reunião de Equipe', 'Agendar com todos os departamentos', true),
(9, 3, 'Orçamento', 'Revisar projeções financeiras', false),

-- Itens para a lista "Estudos de Programação" (user 3)
(10, 4, 'Algoritmos', 'Estudar estruturas de dados', false),
(11, 4, 'Banco de Dados', 'Praticar consultas SQL avançadas', true),
(12, 4, 'Design Patterns', 'Revisar padrões de projeto', false),

-- Itens para a lista "Projetos de TI" (user 4)
(13, 5, 'Migração de Servidores', 'Planejar migração para cloud', false),
(14, 5, 'Segurança', 'Auditar políticas de acesso', true),
(15, 5, 'Monitoramento', 'Configurar alertas no New Relic', false),

-- Itens para a lista "Configurações DevOps" (user 5)
(16, 6, 'CI/CD Pipeline', 'Configurar deploy automático', true),
(17, 6, 'Contêinerização', 'Dockerizar aplicações legacy', false),
(18, 6, 'Infra como Código', 'Atualizar scripts Terraform', false);

joao_dev: "Dev@1234"

maria_admin: "Admin@5678"

carlos_user: "User@9012"

ana_tech: "Tech#3456"

pedro_devops: "DevOps$7890"