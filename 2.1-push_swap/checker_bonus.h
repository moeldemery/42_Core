/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   checker.h                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: meldemir <meldemir@student.42berlin.d      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/16 21:34:26 by meldemir          #+#    #+#             */
/*   Updated: 2026/01/16 21:34:27 by meldemir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef CHECKER_BONUS_H
# define CHECKER_BONUS_H

# include "arg_support.h"
# include "libft/get_next_line.h"
# include "push_swap.h"
# include <stdlib.h>
# include <unistd.h>

void	ft_do_check(t_d_list **stack_a, t_d_list **stack_b);
int		ft_execute_action(char *cmd, t_d_list **stack_a, t_d_list **stack_b);

#endif
