/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   checker.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: meldemir <meldemir@student.42berlin.d      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/16 21:34:10 by meldemir          #+#    #+#             */
/*   Updated: 2026/01/16 21:34:12 by meldemir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "checker.h"

int	main(int argc, char **argv)
{
	t_d_list	*stack_a;
	t_d_list	*stack_b;
	int			i;

	stack_a = NULL;
	stack_b = NULL;
	i = 1;
	if (argc == 2 && argv[1][0])
	{
		if (!ft_proccess_arg_split(argv[1], &stack_a))
			return (ft_putstr_fd("Error\n", 2));
	}
	else if (argc > 2)
	{
		while (i < argc)
			if (!ft_process_arg(argv[i++], &stack_a))
				return (ft_putstr_fd("Error\n", 2));
	}
	else
		return (ft_printf("Error\n") != 0);
	ft_list_print(stack_a, DEBUG, "Initial Stack A:");
	ft_list_print(stack_b, DEBUG, "Initial Stack B:");
	ft_do_check(&stack_a, &stack_b);
	return (0);
}

void	ft_do_check(t_d_list **stack_a, t_d_list **stack_b)
{
	char	*cmd;

	while (1)
	{
		cmd = get_next_line(0);
		if (!cmd)
			break ;
		if (!ft_execute_action(cmd, stack_a, stack_b))
		{
			free(cmd);
			free_stack(stack_a);
			free_stack(stack_a);
			ft_putstr_fd("Error\n", 2);
			exit(1);
		}
		free(cmd);
	}
	if (ft_is_sorted(*stack_a) && ft_lstd_size(*stack_b) == 0)
		ft_printf("OK\n");
	else
		ft_printf("KO\n");
}

int	ft_execute_action(char *cmd, t_d_list **stack_a, t_d_list **stack_b)
{
	if (!ft_strncmp("pa\n", cmd, 3))
		ft_pa(stack_a, stack_b);
	else if (!ft_strncmp("pb\n", cmd, 3))
		ft_pb(stack_a, stack_b);
	else if (!ft_strncmp("sa\n", cmd, 3))
		ft_sa(stack_a);
	else if (!ft_strncmp("sb\n", cmd, 3))
		ft_sb(stack_b);
	else if (!ft_strncmp("ss\n", cmd, 3))
		ft_ss(stack_a, stack_b);
	else if (!ft_strncmp("ra\n", cmd, 3))
		ft_ra(stack_a);
	else if (!ft_strncmp("rb\n", cmd, 3))
		ft_rb(stack_b);
	else if (!ft_strncmp("rr\n", cmd, 3))
		ft_rr(stack_a, stack_b);
	else if (!ft_strncmp("rra\n", cmd, 4))
		ft_rra(stack_a);
	else if (!ft_strncmp("rrb\n", cmd, 4))
		ft_rrb(stack_b);
	else if (!ft_strncmp("rrr\n", cmd, 4))
		ft_rrr(stack_a, stack_b);
	else
		return (0);
	return (1);
}
