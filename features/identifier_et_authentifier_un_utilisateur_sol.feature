Feature: Identifier et authentifier un utilisateur SOL
    [Jama](https://parkeon.jamacloud.com/review.req#/r:REV-574/rp:i409777)

  @project-M2 @device-Cloudfare @test_categorie-Smoke
  Scenario Outline: [US1] - En tant qu'utilisateur Sol, je peux m'authentifier sur le système back-office de Comutitres M2 (<hiptest-uid>)
    "**Critères d'Acceptation**"
    - L'utilisateur Sol s'identifie/authentifie sur le système back-office à travers une IHM de saisie de ses informations identifiant (login) et authentifiant (mot de passe).
    - Le système back-office récupère les habilitations de l'utilisateur Sol à partir du référentiel (ici Keycloak) et n'autorise l'utilisateur sol qu'à accéder aux fonctions et aux modules pour lesquels il a des droits.
    - Le système ne demande plus à l'utilisateur sol de saisir à nouveau son login et son mot de passe (pour l'ensemble des modules du back-office et tant que sa session n'est pas fermée)
    Given G_open_browser "CloudFare" "https://auth-sop3.dev-open-payment.fr/auth/realms/sop3/protocol/openid-connect/auth?client_id=CloudFareWeb&redirect_uri=https%3A%2F%2Festatemanagement-sop3.dev-open-payment.fr%2Fsignin-oidc&response_type=code&scope=openid%20profile%20roles&code_challenge=_3V4u-ZB3EwZ7OG5-fjYefU_o22-jSmAw5dNkIwv7Q8&code_challenge_method=S256&response_mode=form_post&nonce=637616706782311375.Zjg2YWIxNzEtZGI5MC00Y2Q5LWEwMjctYmVjZDE4MmQ3ZGNiMWI4ZGM5ZWQtYTViZC00ZTA3LTlhNDUtZWE0ODBkNTVlMTA1&state=CfDJ8E-qlkOrg11LlKtujeNUprUbNiuZgZOGc8u8X3ac4AVH80LAGXdWaLC6o2b2gscoMpnCOkh1VzhcmIS5PDoGM9oFHEfVhIt7P52LY1jzzL2HiMk1X2stWgYjr3DyJHTbI34ogjipbxDGM7Yqvqd0fWfUBhQpzXmVZ0lXOTiRlZOqzwoEkBvwPziKrH46YxGgsKncFnTuiYbWofC4SIwUkbQa7oTqcqX728cjwHBYrYvPjE-MdYcELRsw4tmz6V05ksGA5tT_lVsRkldeE7T8Cq1eyaQu2lYkN19pWWuQFpNfSy-iM52fQifohD1YJFKuDa5senUQN5LjE36l79JuDLpiTIY92BAsTvCgoao8roJuBA0eLZIBWeaMYsmbU1dI1Q7V0tZkUFk6dgNcV1GqBOjDQ-STuL4XxXGvrfZXPtPw&x-client-SKU=ID_NETSTANDARD2_0&x-client-ver=5.5.0.0"
    When W_insert_element "<username>" "dans le champ l'usager"
    And W_insert_element "<password>" "dans le champ password"
    And W_click_on_element "Log In" "le bouton"
    Then T_open_session "<session>" "la session est ouverte"

    Examples:
      | username | password | session | hiptest-uid |
      | etaillacq | w&YDqI`9=qZ8NuH+'F!HcK6@M.q6?XCu | Emilio Taillacq | uid:72569a64-a3dd-49c8-bcec-c9ef05fb9950 |
